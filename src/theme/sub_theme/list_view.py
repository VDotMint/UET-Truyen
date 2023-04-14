"""_summary_
    """
from turtle import bgcolor

import flet as ft


class ListView:
    """_summary_
    """

    LATEST = 0
    HOT = 1

    def __init__(self, name, sort_type=LATEST):
        self.name = name
        self.sort_type = sort_type

        self.content = None
        self.create_content()

    def create_content(self):
        """_summary_
        """
        def items(count):
            items = []
            for i in range(1, count + 1):
                items.append(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Image(
                                    src="assets/data/cover_img/100000.jpg"
                                ),
                                on_click=lambda e: print("Recommend clicked!"),
                            ),
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Text(
                                                "Tên truyện",
                                                color="#000000",
                                                size=15
                                            ),
                                            on_click=lambda e: print("Title clicked!"),
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Chapter xx",
                                                        size=12
                                                    ),
                                                    padding=5,
                                                    on_click=lambda e: print("Chapter clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Thời gian",
                                                        size=12
                                                    ),
                                                    padding=5,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        )
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                bgcolor=ft.colors.WHITE
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        width=200,

                    )
                )
            return items

        recommendation = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            self.name,
                            color="#2980b9",
                            size=30
                        ),
                        ft.Row(
                            items(20),
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                            wrap=True,
                            width=1000
                        ),
                    ]
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            margin=ft.margin.all(0),
            width=1000
        )
        self.content = ft.Container(
            ft.Column(
                [
                    recommendation
                ]
            ),
            alignment=ft.alignment.center,
            # bgcolor=ft.colors.BLACK,
            width=1000,
            padding=40
        )
