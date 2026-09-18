import flet as ft
import flet_geolocator as fg
import httpx


def main(page: ft.Page):
    # Título da janela
    page.title = "Meu Endereço"

    # Cor de fundo
    page.bgcolor = "#101B2D"

    # Centraliza os controles
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Espaçamento interno
    page.padding = 20

    # Serviço de geolocalização
    geo = fg.Geolocator()
    page.services.append(geo)

    # Botão
    botao = ft.Button(
        content="Obter meu endereço"
    )

    # Container do resultado
    cartao_endereco = ft.Container(visible=False)

    def linha(rotulo, valor):
        return ft.Row(
            controls=[
                ft.Text(rotulo, width=90),
                ft.Text(valor or "-", expand=True),
            ]
        )

    async def obter_local(e):
        botao.disabled = True
        cartao_endereco.visible = False
        page.update()

        await geo.request_permission()
        posicao = await geo.get_current_position()

        async with httpx.AsyncClient() as client:
            resposta = await client.get(
                "https://nominatim.openstreetmap.org/reverse",
                params={
                    "format": "jsonv2",
                    "lat": posicao.latitude,
                    "lon": posicao.longitude,
                },
                headers={"User-Agent": "flet-app"},
            )

            dados = resposta.json()

        endereco = dados.get("address", {})

        rua = endereco.get("road")
        numero = endereco.get("house_number")

        if rua and numero:
            rua_numero = f"{rua}, {numero}"
        else:
            rua_numero = rua or "-"

        bairro = endereco.get("suburb") or endereco.get("neighbourhood")
        cidade = endereco.get("city") or endereco.get("town") or endereco.get("village")
        estado = endereco.get("state")
        cep = endereco.get("postcode")
        pais = endereco.get("country")

        cartao_endereco.content = ft.Column(
            controls=[
                ft.Text(
                    "Endereço encontrado",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                linha("Rua", rua_numero),
                linha("Bairro", bairro),
                linha("Cidade", cidade),
                linha("Estado", estado),
                linha("CEP", cep),
                linha("País", pais),
            ]
        )

        cartao_endereco.visible = True
        botao.disabled = False
        page.update()

    botao.on_click = obter_local

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[botao],
        ),
        cartao_endereco,
    )


ft.run(main)