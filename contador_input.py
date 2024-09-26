import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = "Increment Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.theme_mode = 'light'
    
    text_number: TextField = TextField(value=0, text_align=ft.TextAlign.CENTER, width=150)
    
    def decrement(e: ft.ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()
    
    def increment(e: ft.ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1000)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    def on_text_changed(e: ControlEvent) -> None:
        print(e.control.value)

    page.add(TextField(on_change=on_text_changed))

if __name__ == "__main__":
    # ft.app(target=main)
    ft.app(target=main) #view=ft.AppView.WEB_BROWSER)