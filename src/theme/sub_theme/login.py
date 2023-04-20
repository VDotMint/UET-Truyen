import flet as ft

from pyre_base import sign_in
from src.entity.user import UserWrapper


class Login:
    def __init__(self, app):
        self.app = app
        self.content = None
        self.create_content()

    def create_content(self):

        def to_signup(e: ft.ContainerTapEvent):
            self.app.content.content.controls[2] = self.app.signup.content
            self.app.content.update()

        def to_pwforget(e):
            self.app.content.content.controls[2] = self.app.pwforget.content
            self.app.content.update()

        def to_home(e):
            # # verified ##############
            email = self.content.content.content.controls[1].content.value
            pwd = self.content.content.content.controls[2].content.value

            fb_user = sign_in(email, pwd)

            if True:
                # self.app.user = UserWrapper(fb_user)
                self.app.content.content.controls[2] = self.app.home.content
                self.app.content.update()

                self.app.log_in()

        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(
                                "Đăng nhập",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLACK
                            ),
                            alignment=ft.alignment.center,
                            # padding=20
                        ),
                        ft.Container(
                            ft.TextField(
                                label="Email"
                            ),
                        ),
                        ft.Container(
                            ft.TextField(
                                label="Mật khẩu"
                            ),
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.TextButton(
                                        text="Quên mật khẩu",
                                        on_click=to_pwforget
                                    ),
                                    ft.TextButton(
                                        text="Đăng ký mới",
                                        on_click=to_signup
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Đăng nhập",
                                bgcolor=ft.colors.YELLOW,
                                color=ft.colors.BLACK,
                                width=400,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                ),
                                on_click=to_home

                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Đăng nhập bằng Facebook",
                                bgcolor=ft.colors.BLUE,
                                color=ft.colors.WHITE,
                                icon=ft.icons.FACEBOOK,
                                width=400,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Đăng nhập bằng Google",
                                bgcolor=ft.colors.RED,
                                color=ft.colors.WHITE,
                                width=400,
                                icon=ft.icons.MAIL_ROUNDED,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                )
                            ),
                            alignment=ft.alignment.center
                        )
                    ],
                    width=400,
                    alignment=ft.MainAxisAlignment.START,
                ),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                width=600,
                padding=40
            ),
            bgcolor=ft.colors.BLACK12,
            alignment=ft.alignment.center,
            padding=40
        )
