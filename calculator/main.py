import flet as ft
from calculator.ui import CalculatorApp


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()
    page.window.height = 330
    page.window.width = 390
    page.window.resizable = False
    # add application's root control to the page
    page.add(calc)


if __name__ == "__main__":
    ft.app(target=main)
