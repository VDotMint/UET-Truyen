"""_summary_
    """
import flet as ft


class Recommendation:
    """_summary_
    """

    def __init__(self):
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
                                bgcolor=ft.colors.BLACK
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        width=250,
                    )
                )
            return items

        recommendation = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            "Truyện đề cử",
                            color="#2980b9",
                            size=30
                        ),

                        ft.Row(
                            items(5),
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            margin=ft.margin.all(0),
            width=1250
        )
        self.content = ft.Container(
            ft.Column(
                [
                    recommendation
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            # width=1250,
            # height=333
        )
