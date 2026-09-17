import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = 'Navegação'
    
    def view_inicio():
        return ft.View(
            route='/', # Rota da página principal
            appbar=ft.AppBar(title=ft.Text("Início")),
            bgcolor="#221A3D",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=ft.Padding(top=60, bottom=60, left=0, right=0),
            controls=[
                ft.Text("Tela inicial", color="#C9B6F2", size=18),
                ft.ElevatedButton(
                    "Ir para Sobre",
                    # "lambda" -> Forma rápida de criar uma função de uma única linha
                    # Isso porque o "on_click" espera receber uma função 
                    on_click=lambda e: page.navigate("/sobre"),
                    bgcolor="#9B7EDE",
                    color="#221A3D"
                ),
            ],
        )

    def view_sobre():
        return ft.View(
            route='/sobre', # Rota da página principal
            appbar=ft.AppBar(title=ft.Text("Sobre")),
            bgcolor="#221A3D",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=ft.Padding(top=60, bottom=60, left=0, right=0),
            controls=[
                ft.Text("Esta é a tela sobre", color="#9FD3E8")
            ],
        )

    def route_change(e):
        # Reconstrói a pilha de views a partir da rota atual
        page.views.clear()
        page.views.append(view_inicio())

        if page.route == "/sobre":
            page.views.append(view_sobre())

        page.update()
        
    def view_pop(e):
        # Função acionada quando o usuário clica no "Voltar"
        page.views.pop() # Remove a view de toda pilha
        # Após remover é preciso dizer para onde ir "page.views[-1]" ou seja início
        page.navigate(page.views[-1].route)
    
    # Aqui simplesmente conectamos os dois eventos "route_change" e "view_pop"
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change(None) # Constrói a view da rota inicial

ft.run(main)