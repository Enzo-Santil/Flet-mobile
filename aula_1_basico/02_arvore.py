import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Árvore de controles"
        
    # Cor de fundo da página
    page.bgcolor = "#0766FF"
    
    # Define o tamanho da tela
    page.window.width = 320
    page.window.height = 600
    
    # Centralizar os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)
    
    # Container para o cartão de apresentação
    cartao = ft.Container(
        # Contéudo do cartão organizado em coluna (um item embaixo do outro)
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centralizado dentro do cartão
            controls=[
                # Título do cartão: texto maior, negrito e cor de destaque
                ft.Text(
                    "Título do cartão!",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#00AF06",
                ),

                # Texto descritivo (abaixo do título)
                ft.Text(
                    "Descrição do cartão",
                    color="#FFE600"
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            "Ação 1",
                            bgcolor="#FFFEFF",
                            color="#F90000",
                        ),  # Botão de destaque
                        ft.OutlinedButton("Ação 2"),  # Botão secundário
                    ]
                ),
            ]
        ),
        padding=16,  # Espaçamento interno entre o contéudo
        bgcolor="#143b08",  # Cor de fundo
        border_radius=12,  # Arrendondamento de canto
    )
    # Adiciona o cartão á página
    page.add(cartao)

ft.app(target=main)