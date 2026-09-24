import flet as ft
import httpx


def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Tarefas da API"

    # Cor de fundo da página inteira: azul petróleo escuro
    page.bgcolor = "#101B2D"

    # Centraliza os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Lista onde os títulos das tarefas buscadas na API serão exibidos
    lista_view = ft.ListView(expand=True, spacing=6, width=320)

    async def carregar(e):
        # "async def": esta função usa "await" para não travar o app enquanto
        # espera a resposta da rede (entraremos em detalhes no próximo bloco)
        lista_view.controls.clear()
        async with httpx.AsyncClient() as client:
            resposta = await client.get(
                "https://jsonplaceholder.typicode.com/todos", params={"_limit": 10}
            )
            dados = resposta.json()  # texto JSON -> lista de dicts Python (json.loads por baixo dos panos)
        for tarefa in dados:
            lista_view.controls.append(ft.Text(f"• {tarefa['title']}", color="#CDE0F2"))
        # No Flet 1.0, a tela é atualizada automaticamente ao final do handler,
        # mas chamar page.update() explicitamente continua funcionando normalmente.
        page.update()

    page.add(
        # Flet 1.0: ft.ElevatedButton virou apenas ft.Button (o texto vai no
        # 1º argumento posicional ou no parâmetro "content").
        ft.Button("Carregar tarefas", on_click=carregar, bgcolor="#4C8BF5", color="#0B1622"),
        lista_view,
    )


ft.run(main)
