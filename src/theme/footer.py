"""_summary_
    """
import flet as ft


class Footer:
    """_summary_
    """

    def __init__(self):
        self.content = None
        self.create_content()


    def create_content(self):
        """_summary_
        """
        footer = ft.Container(
            ft.Container(
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Container(
                                    ft.Image(
                                        "assets/icons/loading-animation.png",
                                        width=250
                                    ),
                                    alignment=ft.alignment.center,
                                    padding=20
                                ),
                                ft.Row(
                                    [
                                        ft.Text(
                                            "Liên hệ bản quyền",
                                            color="#ffffff"
                                        ),
                                        ft.Text(
                                            "Chính sách bảo mật",
                                            color="#ffffff"
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Container(
                                    ft.Text("Copyright © 2022 UET Truyen", color="#ffffff"),
                                    alignment=ft.alignment.center
                                ),

                            ],
                            width=600
                        ),
                        ft.Column(
                            [
                                ft.Container(
                                    ft.Text("Từ khóa", size=20,  color="#ffffff")
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("Truyện tranh", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Truyen tranh online", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Đọc truyện tranh", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Truyện tranh hot", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Truyện tranh hay", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("Truyện ngôn tình", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Manhwa", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Manga", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("Manhua", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("truyenqq", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("mi2manga", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("doctruyen3q", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("toptruyen", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("cmanga", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("vlogtruyen", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("blogtruyen", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("truyentranhaudio", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                        ft.OutlinedButton("vcomi", style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2))),
                                    ]
                                ),
                            ]
                        )
                    ],
                    # alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0
                ),
                # alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            margin=ft.margin.all(0)
        )

        self.content = ft.Container(
            ft.Column(
                [
                    footer
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK
        )
