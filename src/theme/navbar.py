import os

from settings import *


class NavBar:
    def __init__(self):
        self.content = None
        self.create_content()
        
    def create_content(self):
        navbar = ft.Container(
        ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.HOUSE
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="HOT",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="THEO DÕI",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="LỊCH SỬ",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.PopupMenuButton(
                                ft.OutlinedButton(
                                    text="THỂ LOẠI",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=2)
                                    )
                            )
                            )
                        ),
                        ft.Container(
                            ft.PopupMenuButton(
                                ft.OutlinedButton(
                                    text="XẾP HẠNG",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=2)
                                    )
                            )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="TÌM TRUYỆN",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="CON GÁI",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="CON TRAI",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="TẢI APP",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                text="GROUP",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            height= 50,
            margin=ft.margin.all(0)
        )
        
        self.content = ft.Container(
            ft.Column(
                [
                    navbar
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK
        )