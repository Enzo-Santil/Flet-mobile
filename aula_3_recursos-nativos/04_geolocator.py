#
# 04 - Geolocator: obter o endereço a partir da localização GPS
# Doc oficial: https://flet.dev/docs/services/geolocator/
# Instalar: pip install flet-geolocator httpx

import asyncio

import flet as ft
import flet_geolocator as ftg
import httpx

# Tempo máximo (em segundos) que aceitamos esperar por uma posição NOVA
# antes de desistir e liberar a tela.
GPS_TIMEOUT_SECONDS = 12


async def main(page: ft.Page):
    page.title = "04 - Geolocator: Meu endereço"

    def on_geo_error(e: ft.ControlEvent):
        pass

    geo = ftg.Geolocator(on_error=on_geo_error)
    page.services.append(geo)

    async def obter_endereco(latitude: float, longitude: float) -> str:
        url = "https://nominatim.openstreetmap.org/reverse"

        params = {
            "lat": latitude,
            "lon": longitude,
            "format": "json",
        }

        headers = {
            "User-Agent": "meu-app-flet-exemplo"
        }

        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                url,
                params=params,
                headers=headers,
            )
            resp.raise_for_status()
            dados = resp.json()

        endereco = dados.get("address", {})

        rua = endereco.get("road", "")
        numero = endereco.get("house_number", "")
        bairro = (
            endereco.get("suburb")
            or endereco.get("neighbourhood", "")
        )

        cidade = (
            endereco.get("city")
            or endereco.get("town")
            or endereco.get("village", "")
        )

        estado = endereco.get("state", "")
        cep = endereco.get("postcode", "")
        pais = endereco.get("country", "")

        linha1 = (
            f"{rua}, {numero}".strip(", ")
            if rua
            else ""
        )

        linha2 = bairro

        linha3 = (
            f"{cidade} - {estado}".strip(" -")
            if cidade or estado
            else ""
        )

        linha4 = f"CEP {cep}" if cep else ""
        linha5 = pais

        linhas = [
            linha
            for linha in (
                linha1,
                linha2,
                linha3,
                linha4,
                linha5,
            )
            if linha
        ]

        return (
            "\n".join(linhas)
            if linhas
            else dados.get(
                "display_name",
                "Endereço não encontrado",
            )
        )

    async def obter_posicao_com_timeout(
        config,
    ) -> ftg.GeolocatorPosition:
        
        """
        Pede a posição atual, mas NUNCA deixa a interface travada além de
        GPS_TIMEOUT_SECONDS — mesmo que a chamada nativa de GPS não
        responda ao cancelamento a tempo.

        Levanta TimeoutError (a exceção nativa do Python, não a do asyncio)
        se o tempo estourar.
        """

        task = asyncio.ensure_future(
            geo.get_current_position(
                configuration=config
            )
        )

        done, pending = await asyncio.wait(
            {task},
            timeout=GPS_TIMEOUT_SECONDS,
        )

        if task in pending:
            # Dispara o cancelamento mas NÃO espera ele terminar — é
            # exatamente isso que evita o travamento do asyncio.wait_for.
            task.cancel()

            raise TimeoutError(
                f"sem resposta do GPS em "
                f"{GPS_TIMEOUT_SECONDS}s"
            )
        # A task terminou dentro do prazo: repassa o resultado (ou a
        # exceção original, se o serviço nativo tiver retornado um erro).
        return task.result()

    async def _endereco_seguro(fn, pos) -> str:
        """Chama obter_endereco() tratando erro de rede num só lugar."""
        try:
            return await fn(
                pos.latitude,
                pos.longitude,
            )

        except httpx.HTTPError as ex:
            return (
                f"Coordenadas: "
                f"{pos.latitude}, "
                f"{pos.longitude}\n"
                f"⚠️ Falha ao consultar o endereço."
            )

    busy = False

    async def get_location(e: ft.Event[ft.Button]):
        nonlocal busy

        if busy:
            return

        busy = True
        get_location_button.disabled = True
        progress.visible = True
        status.value = "Solicitando permissão..."
        page.update()

        try:
            try:
                permissao = await geo.request_permission()

            except Exception:
                status.value = (
                    "⚠️ Não foi possível solicitar "
                    "permissão de GPS."
                )
                return

            if permissao in (
                ftg.GeolocatorPermissionStatus.DENIED,
                ftg.GeolocatorPermissionStatus.DENIED_FOREVER,
            ):
                status.value = (
                    "🚫 Permissão de localização negada. "
                    "Ative-a nas configurações do "
                    "dispositivo/navegador para usar "
                    "este recurso."
                )
                return
            # 1) Tenta primeiro a última posição conhecida: normalmente é
            #    instantânea (não depende do GPS responder agora) e já dá
            #    um retorno rápido ao usuário enquanto buscamos uma
            #    atualizada. Se não houver nenhuma posição em cache, apenas
            #    seguimos para a busca "de verdade" abaixo.
            try:
                pos_cache = (
                    await geo.get_last_known_position()
                )

            except Exception:
                pos_cache = None

            if pos_cache:
                status.value = (
                    "📍 Última posição conhecida "
                    "(atualizando...)"
                )
                page.update()
            # 2) Busca uma posição atualizada, com timeout que realmente
            #    libera a tela no prazo (ver obter_posicao_com_timeout).
            status.value = (
                (
                    status.value + "\n"
                    if pos_cache
                    else ""
                )
                + "Obtendo posição atual via GPS... "
                "(isso pode levar alguns segundos)"
            )

            page.update()

            config = ftg.GeolocatorConfiguration(
                accuracy=(
                    ftg.GeolocatorPositionAccuracy.MEDIUM
                ),
                time_limit=ft.Duration(
                    seconds=GPS_TIMEOUT_SECONDS
                ),
            )

            try:
                pos = await obter_posicao_com_timeout(
                    config
                )

            except TimeoutError:
                if pos_cache:
                    # Já temos algo útil pra mostrar (a última posição
                    # conhecida) mesmo sem conseguir atualizar agora.
                    endereco = await _endereco_seguro(
                        obter_endereco,
                        pos_cache,
                    )

                    status.value = (
                        "⏱️ O GPS não respondeu a tempo "
                        "para uma posição atualizada.\n"
                        "Mostrando a última localização "
                        "conhecida:\n\n"
                        f"{endereco}"
                    )

                else:
                    status.value = (
                        "⏱️ O GPS demorou demais para "
                        "responder. Verifique se a "
                        "localização está ativada no "
                        "dispositivo e tente novamente."
                    )

                return

            except Exception as ex:
            # Rede de segurança: qualquer exceção não prevista nos blocos
            # acima cai aqui, é logada (em vez de sumir silenciosamente) e
            # exibida ao usuário, em vez de travar a tela sem explicação.
                status.value = (
                    "⚠️ Não foi possível obter "
                    f"a posição atual: {ex}"
                )
                return

            status.value = (
                "Posição obtida! "
                "Buscando endereço..."
            )

            page.update()

            endereco = await _endereco_seguro(
                obter_endereco,
                pos,
            )

            status.value = (
                "📍 Minha localização:\n\n"
                f"{endereco}"
            )

        except Exception as ex:
            status.value = (
                f"⚠️ Erro inesperado: {ex}"
            )

        finally:
            busy = False
            get_location_button.disabled = False
            progress.visible = False
            page.update()

    get_location_button = ft.Button(
        "Obter minha localização",
        icon=ft.Icons.MY_LOCATION,
        on_click=get_location,
    )

    progress = ft.ProgressRing(
        width=16,
        height=16,
        stroke_width=2,
        visible=False,
    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            get_location_button,
                            progress,
                        ],
                        spacing=10,
                    ),
                    status := ft.Text(
                        selectable=True,
                        size=16,
                    ),
                ],
                spacing=15,
            )
        )
    )


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
    )

