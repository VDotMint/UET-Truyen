import flet as ft

from src.theme.sub_theme.list_view import ListView
from src.theme.sub_theme.recommendation import Recommendation
from src.theme.sub_theme.top import Top


class Hot:
    def __init__(self):
        self.recommendation = Recommendation()
        self.top = Top()
        self.hot = ListView("Truyện hot nhất")

        self.content = None
        self.create_content()

    def create_content(self):
        self.content = ft.Container(
            ft.Column(
                [
                    self.recommendation.content,
                    ft.Container(
                        ft.Row(
                            [
                                self.hot.content,
                                ft.Container(
                                    ft.Column(
                                        [
                                            self.top.content,
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=40

                                    ),
                                    # bgcolor="#000000",
                                    height=1670

                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        # width=100%,
                        alignment=ft.alignment.center,
                        bgcolor="#ffffff"
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            # width=1400
        )