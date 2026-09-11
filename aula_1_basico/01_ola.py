import flet as ft


def main(page: ft.Page):
    page.title = "Meu primeiro app Flet!"
    page.add(ft.Text("Olá, mundo!!"))


ft.app(target=main)