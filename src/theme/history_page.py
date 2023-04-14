import flet as ft

from src.theme.sub_theme.following import Following
from src.theme.sub_theme.history import History
from src.theme.sub_theme.list_view import ListView
from src.theme.sub_theme.recommendation import Recommendation
from src.theme.sub_theme.top import Top


class HistoryPage:
    def __init__(self):
        self.recommendation = Recommendation()
        self.top = Top()
        self.history = ListView("Lịch sử đọc truyện")
        self.following = Following()

        self.content = None
        self.create_content()

    def create_content(self):
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Row(
                            [
                                self.history.content,
                                ft.Container(
                                    ft.Column(
                                        [
                                            self.following.content,
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