import os
from settings import *


class Header:
    def __init__(self):
        self.content = None
        self.create_content()
        
    def create_content(self):
        header = ft.Container(
            ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            ft.Image("assets/icons/loading-animation.png"),
                            padding=ft.padding.only(right=50)
                        ),
                        ft.Container(
                            ft.TextField(
                                hint_text="Tìm truyện...",
                                bgcolor=ft.colors.WHITE38,
                                color=ft.colors.BLACK,
                            )
                        ),
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.SEARCH,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            ),
                        ),
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.LIGHTBULB
                            ),
                            padding=ft.padding.only(left=30)
                        ),
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.COMMENT
                            ),
                        ),
                        ft.Container(
                            ft.TextButton(
                                text="Đăng ký"
                            ),
                        ),
                        ft.Container(
                            ft.TextButton(
                                text="Đăng nhập"
                            ),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.PURPLE_900,
            height= 50,
            margin=ft.margin.all(0)
        )
        
        self.content = ft.Container(
            ft.Column(
                [
                    header
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK
        )

