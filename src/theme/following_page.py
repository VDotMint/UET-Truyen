import flet as ft

from src.theme.sub_theme.history import History
from src.theme.sub_theme.list_view import ListView
from src.theme.sub_theme.recommendation import Recommendation
from src.theme.sub_theme.top import Top


class FollowingPage:
    def __init__(self):
        self.recommendation = Recommendation()
        self.top = Top()
        self.following = ListView("Truyện đang theo dõi")
        self.history = History()

        self.content = None
        self.create_content()

    def create_content(self):
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Row(
                            [
                                self.following.content,
                                ft.Container(
                                    ft.Column(
                                        [
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