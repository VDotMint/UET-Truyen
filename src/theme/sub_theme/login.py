from pyre_base import sign_in
import flet as ft


class Login:
    def __init__(self):
        self.content = None
        self.create_content()

    def create_content(self):
        email = ft.TextField(
            label="Email"
        )
        password = ft.TextField(
            label="Mật khẩu"
        )
        login = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.TextButton(
                                    text="Trang chủ"
                                ),
                                ft.TextButton(
                                    text="Đăng nhập"
                                )
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Đăng nhập",
                                            size=30,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLACK
                                        ),

                                        email,
                                        password,
                                        ft.Row(
                                            [
                                                ft.TextButton(
                                                    text="Quên mật khẩu"
                                                ),
                                                ft.TextButton(
                                                    text="Đăng ký mới"
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END
                                        ),
                                        ft.ElevatedButton(
                                            text="Đăng nhập",
                                            bgcolor=ft.colors.YELLOW,
                                            color=ft.colors.WHITE,
                                            on_click=lambda e: sign_in(email.value, password.value),
                                            width=300
                                        ),
                                        ft.ElevatedButton(
                                            text="Đăng nhập bằng Facebook",
                                            bgcolor=ft.colors.BLUE,
                                            color=ft.colors.BLACK,
                                            icon=ft.icons.FACEBOOK,
                                            width=305
                                        ),
                                        ft.ElevatedButton(
                                            text="Đăng nhập bằng Google",
                                            bgcolor=ft.colors.RED,
                                            color=ft.colors.BLACK,
                                            width=305
                                        )
                                    ]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            margin=ft.margin.all(0)
        )

        self.content = ft.Container(
            ft.Column(
                [
                    login
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
        )
