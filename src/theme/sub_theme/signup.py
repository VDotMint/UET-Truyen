import flet as ft
# from ....src.firebase import create_user


class Signup:
    def __init__(self, app):
        self.app = app
        self.content = None
        self.create_content()

    def create_content(self):
        password = ft.TextField(
            label="Mật khẩu"
        )
        email = ft.TextField(
            label="Email"
        )
        re_password = ft.TextField(
            label="Nhập lại mật khẩu"
        )

        def print_content(e):
            print(password.value, email.value, re_password.value)

        def to_login(e: ft.ContainerTapEvent):
            self.app.content.content.controls[2] = self.app.login.content
            self.app.content.update()

        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(
                                "Đăng ký tài khoản",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLACK
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            email,
                        ),
                        ft.Container(
                            password,
                        ),
                        ft.Container(
                            re_password,
                        ),
                        ft.Container(
                            ft.TextButton(
                                text="Đã có tài khoản! Đăng nhập",
                                on_click=to_login
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Đăng ký",
                                bgcolor=ft.colors.YELLOW,
                                color=ft.colors.BLACK,
                                width=400,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                ),
                                # on_click=to_home

                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Đăng ký bằng Facebook",
                                bgcolor=ft.colors.BLUE,
                                color=ft.colors.WHITE,
                                icon=ft.icons.FACEBOOK,
                                width=400,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                                # on_click=create_user(email.value, password.value)
                            ),
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Đăng ký bằng Google",
                                bgcolor=ft.colors.RED,
                                color=ft.colors.WHITE,
                                icon=ft.icons.MAIL_ROUNDED,
                                width=400,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            )
                        )
                    ],
                    width=400,
                    alignment=ft.MainAxisAlignment.START
                ),
                width=600,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                padding=40
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            padding=40
        )