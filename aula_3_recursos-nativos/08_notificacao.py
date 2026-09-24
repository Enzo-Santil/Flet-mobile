# 08 - Banner: notificação persistente no topo da tela
# Doc oficial: https://docs.flet.dev/controls/banner

# Nota importante: isto NÃO é uma notificação nativa do sistema operacional
# (aquelas que aparecem na barra de notificações do Android/iOS mesmo com o
# app em segundo plano). É um "Banner" — um aviso in-app, persistente, que
# fica preso ao topo da área de conteúdo enquanto o app está aberto. Para
# notificações de sistema de verdade, seria necessário um pacote separado
# (fora do escopo core do Flet).


import flet as ft
import asyncio

async def main(page: ft.Page):

    page.title = "08 - Banner: Notificação no topo"
    page.padding = 20

    # Fecha a notificação
    def fechar(e):
        page.pop_dialog()

    # Exibe a notificação
    async def notificar(e):

        mensagem = campo.value.strip()

        if not mensagem:
            mensagem = "Digite uma mensagem!"

        banner = ft.Banner(
            leading=ft.Icon(
                ft.Icons.NOTIFICATIONS_ACTIVE,
                color=ft.Colors.BLUE,
            ),

            content=ft.Text(
                mensagem,
                size=16,
            ),

            actions=[
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    tooltip="Fechar",
                    on_click=fechar,
                )
            ],
        )

        # Exibe a notificação
        page.show_dialog(banner)

        # Aguarda 5 segundos
        await asyncio.sleep(5)

        # Fecha automaticamente caso ainda esteja aberta
        if banner.open:
            page.pop_dialog()

    # Campo para digitar a mensagem
    campo = ft.TextField(
        label="Digite a notificação",
        hint_text="Ex.: Atividade entregue com sucesso!",
        width=400,
    )

    # Botão
    botao = ft.Button(
        "Exibir notificação",
        icon=ft.Icons.NOTIFICATIONS,
        on_click=notificar,
    )

    # Interface
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "🔔 Sistema de Notificação",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        "Digite uma mensagem e clique no botão."
                    ),

                    campo,

                    botao,
                ],
                spacing=20,
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)