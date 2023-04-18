import flet as ft

from src.theme.sub_theme.following import Following
from src.theme.sub_theme.history import History
from src.theme.sub_theme.list_view import ListView
from src.theme.sub_theme.recommendation import Recommendation
from src.theme.sub_theme.top import Top


class Home:
    def __init__(self, app):
        self.content = None
        self.recommendation = Recommendation(app)

        self.latest = ListView(app, "Truyện mới cập nhật")
        self.following = Following(app)
        self.top = Top(app)
        self.history = History(app)

        self.create_content()

    def create_content(self):
        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        self.recommendation.content,
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Container(
                                        self.latest.content,
                                        height=1460
                                    ),
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
                                        height=1400

                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            # alignment=ft.alignment.center,
                            bgcolor="#ffffff"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                alignment=ft.alignment.center,
                width=1400
            ),
            alignment=ft.alignment.center,
        )
