"""_summary_
    """
import flet as ft

ACTIVE_BG_COLOR = "#ffffff"
BG_COLOR = "#CCCCCC"
BORDER_COLOR = "#C0C0C0"
ACTIVE_BORDER_COLOR = "#33cccc"


class Top:
    """_summary_
    """

    def __init__(self):
        self.content = None
        self.tabs = None
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
                                        ft.Text(
                                            "0" + str(i),
                                            color="#2980b9",
                                            size=20,
                                        ),
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
                                                ft.Row(
                                                    [
                                                        ft.Container(
                                                            ft.Text(
                                                                "Chapter xx",
                                                                size=15,
                                                                color="#000000",
                                                            ),
                                                            on_click=lambda e: print("Chapter clicked!"),
                                                        ),
                                                        ft.Container(
                                                            ft.Row(
                                                                [
                                                                    ft.Icon(
                                                                        name=ft.icons.REMOVE_RED_EYE,
                                                                        color="#C0C0C0",
                                                                        size=12
                                                                    ),
                                                                    ft.Text(
                                                                        "100K",
                                                                        color="#C0C0C0",
                                                                        size=15
                                                                    ),
                                                                ],
                                                                spacing=0,
                                                            )
                                                        )
                                                    ],
                                                    width=180,
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND
                                        ),
                                    ]
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        border=ft.border.only(
                            left=ft.border.BorderSide(1, "#C0C0C0"),
                            right=ft.border.BorderSide(1, "#C0C0C0"),
                            bottom=ft.border.BorderSide(1, "#C0C0C0")
                        ),
                        height=80,
                        width=300,
                        padding=10
                    )
                )
            return items

        def change_top(e: ft.ContainerTapEvent):
            for x in self.tabs.controls:
                x.bgcolor = BG_COLOR

            e.control.bgcolor = ACTIVE_BG_COLOR

            self.tabs.update()

        self.tabs = ft.Row(
            [
                ft.Container(
                    ft.Text(
                        "Top Tháng",
                        color="#000000",
                        size=15
                    ),
                    border=ft.border.only(
                        left=ft.border.BorderSide(1, "#C0C0C0"),
                        bottom=ft.border.BorderSide(1, "#C0C0C0"),
                        top=ft.border.BorderSide(1, BORDER_COLOR)
                    ),
                    bgcolor=ACTIVE_BG_COLOR,
                    width=97,
                    height=50,
                    alignment=ft.alignment.center,
                    on_click=change_top,
                ),
                ft.Container(
                    ft.Text(
                        "Top Tuần",
                        color="#000000",
                        size=15
                    ),
                    border=ft.border.only(
                        left=ft.border.BorderSide(1, "#C0C0C0"),
                        bottom=ft.border.BorderSide(1, "#C0C0C0"),
                        top=ft.border.BorderSide(1, BORDER_COLOR),
                    ),
                    bgcolor=BG_COLOR,
                    width=97,
                    height=50,
                    alignment=ft.alignment.center,
                    on_click=change_top,
                ),
                ft.Container(
                    ft.Text(
                        "Top Ngày",
                        color="#000000",
                        size=15
                    ),
                    border=ft.border.only(
                        left=ft.border.BorderSide(1, "#C0C0C0"),
                        right=ft.border.BorderSide(1, "#C0C0C0"),
                        bottom=ft.border.BorderSide(1, "#C0C0C0"),
                        top=ft.border.BorderSide(1, BORDER_COLOR),
                    ),
                    bgcolor=BG_COLOR,
                    width=96,
                    height=50,
                    alignment=ft.alignment.center,
                    on_click=change_top,
                )
            ],
            spacing=0
        )

        top = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            self.tabs,
                            height=50,
                            width=300,
                        ),
                        ft.Column(
                            items(7),
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
                    top
                ],
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
            width=300,
        )
