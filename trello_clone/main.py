import flet as ft
from flet import Page, colors, Container, Icon, Text
from flet import AppView, AppBar, PopupMenuButton, PopupMenuItem
from flet import margin, icons


class TrelloApp:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("Trolli", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25),
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()


def main(page: Page):
    page.title = "Flet Trello Clone"
    page.padding = 20
    page.bgcolor = colors.BLUE_GREY_200

    # create application instance
    app = TrelloApp(page)
    page.add(app)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

if __name__ == "__main__":
    ft.app(main, view=AppView.WEB_BROWSER)
