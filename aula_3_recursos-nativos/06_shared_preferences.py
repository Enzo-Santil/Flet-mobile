#
# 06 - SharedPreferences: salvar dados simples que persistem entre execuções
# Doc oficial: https://flet.dev/docs/services/sharedpreferences

import flet as ft

async def main(page: ft.Page):
    page.title = "06 - SharedPreferences: Armazenamento local"
    prefs = ft.SharedPreferences()

    async def save_name(e: ft.Event[ft.Button]):
        nome = (name_field.value or "").strip()
        if not nome:
            status.value = "⚠️ Digite um nome antes de salvar."
            return
        try:
            await prefs.set("nome_usuario", nome)
        except Exception as ex:
            status.value = f"⚠️ Erro ao salvar: {ex}"
            return
        status.value = "✅ Nome salvo! Feche e abra o app de novo para conferir."

    async def load_name(e: ft.Event[ft.Button]):
        try:
            saved = await prefs.get("nome_usuario")
        except Exception as ex:
            status.value = f"⚠️ Erro ao carregar: {ex}"
            return
        status.value = f"👋 Nome salvo: {saved}" if saved else "Nenhum nome salvo ainda."

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    name_field := ft.TextField(label="Seu nome"),
                    ft.Row(
                        controls=[
                            ft.Button("Salvar", on_click=save_name),
                            ft.Button("Carregar", on_click=load_name),
                        ]
                    ),
                    status := ft.Text(),
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)
