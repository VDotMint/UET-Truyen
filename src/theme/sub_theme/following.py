"""_summary_
    """
from turtle import bgcolor

import flet as ft


class Following:
    """_summary_
    """

    def __init__(self):
        self.content = None
        self.create_content()

    def create_content(self):
        """
        iterate truyện
        """
        def items(count):
            items = []
            for i in range(1, count + 1):
                items.append(
                    ft.Container(
                        ft.Row(
                            [
                                ft.Row(
                                    [
                                        ft.Container(
                                            ft.Image(
                                                src="assets/data/cover_img/100000.jpg",
                                            ),
                                            on_click=lambda e: print("Cover truyen clicked!"),
                                        ),
                                        ft.Column(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Tên truyện",
                                                        size=15,
                                                        color="#000000",
                                                    ),
                                                    on_click=lambda e: print("Tên truyện clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Chapter xx",
                                                        size=15,
                                                        color="#000000",
                                                    ),
                                                    on_click=lambda e: print("Chapter clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Đọc tiếp Chapter xx",
                                                        size=10,
                                                        color=ft.colors.BLACK54,
                                                    ),
                                                    on_click=lambda e: print("Đọc tiếp clicked!"),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND
                                        ),
                                    ]
                                ),
                                ft.Text(
                                    "Bao lâu trước",
                                    size=10,
                                    color="#C0C0C0"
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        border=ft.border.only(
                            left=ft.border.BorderSide(1,"#C0C0C0"),
                            right=ft.border.BorderSide(1, "#C0C0C0"),
                            bottom=ft.border.BorderSide(1, "#C0C0C0")
                        ),
                        height=80,
                        width=300,
                        padding=10
                    )
                )
            return items

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
                                        on_click=lambda e: print("Xem tất cả clicked!"),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND
                            ),
                            height=50,
                            width=300,
                            border=ft.border.all(1,"#C0C0C0")
                        ),
                        ft.Column(
                            items(5),
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
