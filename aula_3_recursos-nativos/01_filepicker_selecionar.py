# 01 - FilePicker: selecionar um ou vários arquivos do dispositivo
# Doc oficial: https://flet.dev/docs/services/filepicker

import flet as ft

async def main(page: ft.Page):
    page.title = "01 - FilePicker: Selecionar arquivos"

    async def pick_files(e: ft.Event[ft.Button]):
        # allow_multiple=True permite selecionar vários arquivos de uma vez.
        # Em app web (navegador), lembre-se: um FilePicker só abre durante o
        # tratamento de um clique real do usuário. Se em algum outro exemplo
        # seu você chamar pick_files() fora de um on_click direto (ex.: depois
        # de um await anterior), use uma "client action" (ft.PickFiles) — veja
        # a seção "Picking files with a client action" na doc do FilePicker.
        try:
            files = await ft.FilePicker().pick_files(allow_multiple=True)
        except Exception as ex:
            result.value = f"⚠️ Não foi possível abrir o seletor de arquivos: {ex}"
            return

        if files:
            result.value = "\n".join(f"📄 {f.name} ({f.size} bytes)" for f in files)
        else:
            result.value = "Nenhum arquivo selecionado."

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Toque para escolher arquivos do celular:"),
                    ft.Button(
                        "Selecionar arquivos",
                        icon=ft.Icons.UPLOAD_FILE,
                        on_click=pick_files,
                    ),
                    # O walrus (:=) cria a variável `result` já dentro da lista
                    # de controles e a deixa acessível fora do Column também.
                    result := ft.Text(),
                ]
            )
        )
    )
    # Não é preciso chamar page.update() aqui: desde o 1.0, o Flet atualiza a
    # tela automaticamente ao final de main() e de cada handler de evento.


if __name__ == "__main__":
    ft.run(main)
