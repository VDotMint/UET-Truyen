import flet as ft

from src.theme.sub_theme.list_view import ListView


class FilterPage:
    def __init__(self, app):
        self.content = None

        self.list_view = ListView(app, "Lọc")

        self.create_content()

    def change_name(self, name):
        self.list_view.change_name(name)
        self.content.update()

    def create_content(self):
        self.content = ft.Container(
            self.list_view.content,
            alignment=ft.alignment.center
        )
