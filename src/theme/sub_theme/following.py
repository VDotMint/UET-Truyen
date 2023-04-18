"""_summary_
    """
from turtle import bgcolor
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.entity.comic_modules.comic_getter import ComicGetters
import flet as ft

from src.theme.sub_theme.extra import SmallCard


class Following:
    """_summary_
    """

    def __init__(self, app):
        self.content = None

        self.app = app
        self.following_list = [100004, 100008, 100005, 100006, 100001]

        self.create_content()

    def create_content(self):
        """
        iterate truyện
        """
        def items(count, comic_list):
            items = []
            for i in range(count):
                items.append(SmallCard(self.app, comic_list[i]))
            return items

        def change_page(e):
            for x in self.app.navbar.tabs.controls:
                x.content.bgcolor = self.app.navbar.DEFAULT_COLOR

            self.app.navbar.tabs.controls[2].content.bgcolor = self.app.navbar.ACTIVE_COLOR

            self.app.content.content.controls[2] = self.app.following_page.content
            self.app.content.update()

        following = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(
                                        "Truyện đang theo dõi",
                                        color="#2980b9",
                                        size=20
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            "Xem tất cả",
                                            color="#000000",
                                            size=10
                                        ),
                                        on_click=change_page,
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND
                            ),
                            height=50,
                            width=300,
                            border=ft.border.all(1,"#C0C0C0")
                        ),
                        ft.Column(
                            items(len(self.following_list), self.following_list),
                            spacing=0
                        ),
                    ],
                    spacing=0
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            margin=ft.margin.all(0)
        )
        self.content = ft.Container(
            ft.Column(
                [
                    following
                ],
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
            width=300,
        )
