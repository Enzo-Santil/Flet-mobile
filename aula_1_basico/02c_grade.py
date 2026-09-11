import flet as ft

def card_produto(nome, preco):
    return ft.Container(
        width=140,
        height=140,
        padding=12,
        bgcolor="#FFF3E0",
        border_radius=12,
        content=ft.Column(
            # Alinhamento horizotal
            alignment=ft.MainAxisAlignment.CENTER,
            # Alinhamento vertical
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.SHOPPING_BAG, size=22, color="#3CA42E"),
                ft.Text(nome, weight=ft.FontWeight.BOLD, color="#3CA42E"),
                ft.Text(f"R$ {preco:.2f}", color="#6D4C41"),
            ],
        ),
    )    

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Prateleira"
        
    # Cor de fundo da página
    page.bgcolor = "#4E004E"
    
    # Define o tamanho da tela
    page.window.width = 320
    page.window.height = 600
    
    # Centralizar os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)
    
    # Tupla (nome, preço)
    produtos = [
        ("Caneta", 3.5),
        ("Caderno", 12.9),
        ("Mochila", 89.9),
        ("Estojo", 24.9),
        ("Régua", 5.0),
        ("Borracha", 2.5),
    ]
    
    page.add(
        ft.Row(
            # Permite rolar horizontalmente
            scroll=ft.ScrollMode.HIDDEN,  # Sim. em: Celular

            # Centraliza os cartões em linha
            alignment=ft.MainAxisAlignment.CENTER,

            # Laço para gerar os cards
            controls=[card_produto(nome, preco) for nome, preco in produtos]
        )
    )

ft.app(target=main)