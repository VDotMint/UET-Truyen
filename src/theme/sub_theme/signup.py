import flet as ft


class Signup:
    def __init__(self):
        self.content = None
        self.create_content()

    def create_content(self):
        signup = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.TextButton(
                                    text="Trang chủ"
                                ),
                                ft.TextButton(
                                    text="Đăng ký"
                                )
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Đăng ký tài khooản",
                                            size=30,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLACK
                                        ),
                                        ft.TextField(
                                            label="Email"
                                        ),
                                        ft.TextField(
                                            label="Mật khẩu"
                                        ),
                                        ft.TextField(
                                            label="Nhập lại mật khẩu"
                                        ),
                                        ft.ElevatedButton(
                                            text="Đăng ký bằng Facebook",
                                            bgcolor = ft.colors.BLUE,
                                            color=ft.colors.BLACK,
                                            icon=ft.icons.FACEBOOK,
                                            width=305
                                        ),
                                        ft.ElevatedButton(
                                            text="Đăng ký bằng Google",
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
                    signup
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
        )
