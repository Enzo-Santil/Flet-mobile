# 02 - Battery: nível, estado e modo de economia de energia
# Doc oficial: https://flet.dev/docs/services/battery

import flet as ft

async def main(page: ft.Page):
    page.title = "02 - Battery: Status da bateria"
    battery = ft.Battery()
    page.services.append(battery)  # manter referência do serviço

    async def refresh_info(e: ft.Event[ft.Button] = None):
        try:
            level = await battery.get_battery_level()
            state = await battery.get_battery_state()
            save_mode = await battery.is_in_battery_save_mode()
        except Exception as ex:
            # Em plataformas sem suporte a este recurso (ex.: alguns
            # navegadores), o service pode lançar exceção em vez de apenas
            # retornar None.
            info.value = f"⚠️ Não foi possível ler dados da bateria: {ex}"
            return

        info.value = (
            f"🔋 Nível: {level}%\n"
            f"⚡ Estado: {state.name}\n"
            f"💤 Economia de energia: {'Ligada' if save_mode else 'Desligada'}"
        )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    info := ft.Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                    ft.Button("Atualizar informações", on_click=refresh_info),
                ]
            )
        )
    )
    # Chamado sem argumento de evento (e=None) para popular a tela assim que
    # o app abre — funciona porque handlers em 1.0 podem receber 0 ou 1
    # argumento.
    await refresh_info()


if __name__ == "__main__":
    ft.run(main)
