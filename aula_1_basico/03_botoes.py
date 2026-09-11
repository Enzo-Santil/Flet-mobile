import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Formulário simples"
    
    # Cor de fundo da página
    page.bgcolor = "#EAF4F4"
    
    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)
    
    # Campo de texto para o nome
    nome = ft.TextField(
        label="Seu nome",
        width=280, # Largura do campo
        color="#2D3142", # Cor do texto
        # Cor do label ("Seu nome")
        label_style=ft.TextStyle(color="#000000"),
        border_color="#760989", # Cor da borda
        # Cor quando em campo em foco (Clicado ou ativado)
        focused_border_color="#760989",
    )
    
    # CheckBox de aceite dos termos
    aceite = ft.Checkbox(
        label="Aceito os termos",
        check_color="#FFFFFF", # Cor do check (visto)
        active_color="#760989", # Cor do check (quando marcado)
        # Cor do label ("Aceito os termos")
        label_style=ft.TextStyle(color="#2D3142"),
    )
    
    # Texto de resultado (Após enviar)
    resultado = ft.Text(color="#760989")
    
    def enviar(e):
        # Função de envio dos dados com validações
        if not nome.value:
            nome.error_text = "Preencha seu nome"
            page.update()
            return
            
        nome.error_text = None
        resultado.value = (
            f"Obrigado, {nome.value}!"
            if aceite.value
            else "Você precisa aceitar os termos."
        )
        page.update()
        
    # Construção dos elementos
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                nome,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[aceite],
                ),
                
                # Botão "Enviar"
                ft.ElevatedButton(
                    "Enviar",
                    on_click=enviar, # Ao clicar chama a função enviar
                    bgcolor="#760989",
                    color="#FFFFFF",
                ),
                # Exibição dos resultados
                resultado,
            ]
        )
    )

ft.app(target=main)