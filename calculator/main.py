import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value="Hello, World!", size=30, font_family="Consolas"))

ft.app(target=main)