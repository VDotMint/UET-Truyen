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
                                        "assets/icons/loading-animation.png", width=150)
                                ),
                                ft.Row(
                                    [
                                        ft.TextButton(
                                            text="Liên hệ bản quyền"
                                        ),
                                        ft.TextButton(
                                            text="Chính sách bảo mật"
                                        ),
                                    ]
                                ),
                                ft.Container(
                                    ft.Text("Copyright © 2022 UetTruyen")
                                ),
                            ]
                        ),
                        ft.Column(
                            [
                                ft.Container(
                                    ft.Text("Từ khóa")
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("Truyện tranh"),
                                        ft.OutlinedButton(
                                            "Truyen tranh online"),
                                        ft.OutlinedButton("Đọc truyện tranh"),
                                        ft.OutlinedButton("Truyện tranh hot"),
                                        ft.OutlinedButton("Truyện tranh hay"),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("Truyện ngôn tình"),
                                        ft.OutlinedButton("Manhwa"),
                                        ft.OutlinedButton("Manga"),
                                        ft.OutlinedButton("Manhua"),
                                        ft.OutlinedButton("truyenqq"),
                                        ft.OutlinedButton("mi2manga"),
                                        ft.OutlinedButton("doctruyen3q"),
                                        ft.OutlinedButton("toptruyen"),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("cmanga"),
                                        ft.OutlinedButton("vlogtruyen"),
                                        ft.OutlinedButton("blogtruyen"),
                                        ft.OutlinedButton("truyentranhaudio"),
                                        ft.OutlinedButton("vcomi"),
                                    ]
                                ),
                            ]
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
