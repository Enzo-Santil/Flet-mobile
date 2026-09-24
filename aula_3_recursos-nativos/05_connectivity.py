#
# 05 - Connectivity: status da conexão (wifi, dados móveis, offline)
# Doc oficial: https://flet.dev/docs/services/connectivity

import flet as ft

async def main(page: ft.Page):
    page.title = "05 - Connectivity: Status da conexão"
    connectivity = ft.Connectivity()

    async def refresh(e=None):
        try:
            results = await connectivity.get_connectivity()
        except Exception as ex:
            status.value = f"⚠️ Não foi possível checar a conectividade: {ex}"
            return
        status.value = "📶 Conectividade: " + ", ".join(r.value for r in results)

    async def on_change(e: ft.ConnectivityChangeEvent):
        changes.value = "🔄 Mudou para: " + ", ".join(r.value for r in e.connectivity)
        await refresh()

    connectivity.on_change = on_change
    page.services.append(connectivity)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    status := ft.Text(),
                    ft.Button("Verificar conexão agora", on_click=refresh),
                    changes := ft.Text(),
                ]
            )
        )
    )
    await refresh()


if __name__ == "__main__":
    ft.run(main)
