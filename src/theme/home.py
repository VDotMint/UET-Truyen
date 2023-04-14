import flet as ft

from src.theme.sub_theme.following import Following
from src.theme.sub_theme.history import History
from src.theme.sub_theme.list_view import ListView
from src.theme.sub_theme.recommendation import Recommendation
from src.theme.sub_theme.top import Top


class Home:
    def __init__(self):
        self.content = None
        self.recommendation = Recommendation()

        self.latest = ListView("Truyện mới cập nhật")
        self.following = Following()
        self.top = Top()
        self.history = History()

        self.create_content()

    def create_content(self):
        self.content = ft.Container(
            ft.Column(
                [
                    self.recommendation.content,
                    ft.Container(
                        ft.Row(
                            [
                                self.latest.content,
                                ft.Container(
                                    ft.Column(
                                        [
                                            self.following.content,
                                            self.history.content,
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
