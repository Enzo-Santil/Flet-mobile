## 03 - HapticFeedback: vibrações e toques hápticos
# Doc oficial: https://flet.dev/docs/services/hapticfeedback

import flet as ft

def main(page: ft.Page):
    page.title = "03 - HapticFeedback: Vibração"
    hf = ft.HapticFeedback()
    page.services.append(hf)

    async def _run_safely(coro_fn, label: str):
        """Executa uma chamada de vibração e mostra erro amigável se falhar."""
        try:
            await coro_fn()
            status.value = f"✅ {label} disparado."
        except Exception as ex:
            status.value = f"⚠️ {label} não suportado neste dispositivo: {ex}"

    async def light_impact(e):
        await _run_safely(hf.light_impact, "Impacto leve")

    async def medium_impact(e):
        await _run_safely(hf.medium_impact, "Impacto médio")

    async def heavy_impact(e):
        await _run_safely(hf.heavy_impact, "Impacto forte")

    async def selection_click(e):
        await _run_safely(hf.selection_click, "Clique de seleção")

    async def vibrate(e):
        await _run_safely(hf.vibrate, "Vibração")

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Toque nos botões e sinta a vibração do celular:"),
                    ft.Button("Impacto leve", on_click=light_impact),
                    ft.Button("Impacto médio", on_click=medium_impact),
                    ft.Button("Impacto forte", on_click=heavy_impact),
                    ft.Button("Clique de seleção", on_click=selection_click),
                    ft.Button("Vibrar", on_click=vibrate),
                    status := ft.Text(),
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)
