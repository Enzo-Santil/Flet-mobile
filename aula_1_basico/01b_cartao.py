import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de apresentação"
    
    # Define o tamanho da tela
    page.window.width = 320
    page.window.height = 600
    
    # Cor de fundo da tela
    page.bgcolor = "#2B1B3D"
    
    # Centralizar elementos
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Padding
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)
    
    # Criação dos elementos da página
    page.add(
        # Nome em destaque
        ft.Text(
            "Flaquito Lopez!!",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#02820A",
            text_align=ft.TextAlign.CENTER,
        ),
        ft.Text(
            "Estudante de Desenvolvimento de sistemas!",
            size=28,
            color="#B10000",
            text_align=ft.TextAlign.CENTER,
        ),
    )
# Inicia a aplicação
ft.app(target=main)