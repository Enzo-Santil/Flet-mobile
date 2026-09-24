#
# 07 - Flashlight: ligar/desligar a lanterna do celular
# Doc oficial: https://flet.dev/docs/services/flashlight/
# Instalar: pip install flet-flashlight

import flet as ft
import flet_flashlight as ffl

def main(page: ft.Page):
    page.title = "07 - Flashlight: Lanterna"
    flashlight = ffl.Flashlight()

    async def turn_on(e):
        try:
            await flashlight.on()
        except Exception as ex:
            status.value = f"⚠️ Lanterna indisponível neste dispositivo: {ex}"
            return
        status.value = "🔦 Lanterna LIGADA"

    async def turn_off(e):
        try:
            await flashlight.off()
        except Exception as ex:
            status.value = f"⚠️ Lanterna indisponível neste dispositivo: {ex}"
            return
        status.value = "⚫ Lanterna DESLIGADA"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button("Ligar lanterna", icon=ft.Icons.FLASHLIGHT_ON, on_click=turn_on),
                    ft.Button("Desligar lanterna", icon=ft.Icons.FLASHLIGHT_OFF, on_click=turn_off),
                    status := ft.Text(),
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)
