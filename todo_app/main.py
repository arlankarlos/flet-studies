import flet as ft
from todoapp import TodoApp


def main(page: ft.Page):
    page.title = "Todo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 700
    page.window.height = 450
    
    # create application instance
    todo = TodoApp()
    
    # add application's root control to the page
    page.add(todo)

if __name__ == "__main__":
    ft.app(target=main)
