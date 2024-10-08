import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Sign Up"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.ThemeMode.SYSTEM
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False

    # Setup our fields
    text_username: TextField = TextField(
        label="Username", text_align=ft.TextAlign.LEFT, width=200
    )
    text_password: TextField = TextField(
        label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True
    )
    checkbox_signup: Checkbox = Checkbox(
        label="I agree to stuff and things", value=False
    )
    button_submit: ElevatedButton = ElevatedButton(
        text="Sign Up", width=200, disabled=True
    )

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.validate()

    def submit(e: ControlEvent) -> None:
        print("Username: " + text_username.value)
        print("Password: " + text_password.value)
        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome: {text_username.value}", size=20)],
            )
        )

    # Link the functions to our UI
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the page sign-up page
    # page.add(
    #     Row(
    #         controls=[
    #             Column([text_username, text_password, checkbox_signup, button_submit])
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )
    page.add(
        Column(
            controls=[
                Row(controls=
                    [text_username, text_password, checkbox_signup, button_submit],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
    )
    # page.add(
    #     Row(
    #         [Column(
    #             text_username, text_password, checkbox_signup, button_submit
    #         )],

    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )


if __name__ == "__main__":
    ft.app(target=main)
