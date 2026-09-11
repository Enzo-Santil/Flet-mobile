import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Cadastro"

    # Cor de fundo da página inteira: roxo escuro
    page.bgcolor = "#241E3D"

    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Campo de texto para o nome
    nome = ft.TextField(
        label="Nome",
        width=280,
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#D9A9D1"),
        border_color="#2C00B1",
        focused_border_color="#B388EB",
    )

    # Campo de texto para o e-mail
    email = ft.TextField(
        label="E-mail",
        width=280,
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#D9A9D1"),
        border_color="#2C00B1",
        focused_border_color="#B388EB",
    )

    # Dropdown de seleção de estado
    estado = ft.Dropdown(
        label="Estado",
        width=280,
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#D9A9D1"),
        border_color="#2C00B1",
        options=[ft.dropdown.Option("SP"), ft.dropdown.Option("RJ"), ft.dropdown.Option("MG")],
    )

    # Checkbox de aceite para receber novidades
    novidades = ft.Checkbox(
        label="Quero receber novidades",
        active_color="#0714FF",
        label_style=ft.TextStyle(color="#E5DCF5"),
    )

    # Texto de resumo, exibido após o cadastro
    resumo = ft.Text(color="#FD0101")

    def cadastrar(e):
        linha1= f"{nome.value} ({email.value}) — {estado.value or 'sem estado'} — "
        linha2= f"{estado.value or 'sem estado'}"
        linha3= f"novidades: {'sim' if novidades.value else 'não'}"
        resumo.value = f"{linha1}\n{linha2}\n{linha3}"
        page.update()

    # Column explícita centralizando todos os controles, inclusive o checkbox
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                nome,
                email,
                estado,
                ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[novidades]),
                ft.ElevatedButton(
                    "Cadastrar",
                    on_click=cadastrar,
                    bgcolor="#D9A9D1",
                    color="#241E3D",
                ),
                resumo,
            ],
        )
    )

ft.run(main)