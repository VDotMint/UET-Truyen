import flet as ft


class PWForget:
    def __init__(self, app):
        self.app = app
        self.content = None
        self.create_content()

    def create_content(self):
        def to_login(e: ft.ContainerTapEvent):
            self.app.content.content.controls[2] = self.app.login.content
            self.app.content.update()

        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(
                                "Vui lòng nhập Email",
                                size=25,
                                color=ft.colors.BLUE
                            )
                        ),
                        ft.Container(
                            ft.TextField(
                                label="Email"
                            ),
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                text="Xác nhận",
                                bgcolor=ft.colors.BLUE,
                                color=ft.colors.WHITE,
                                width=400,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                ),
                                on_click=to_login
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.Image(src="assets/gui/confirm.gif"),
                            alignment=ft.alignment.center
                        )
                    ],
                    width=400,
                    alignment=ft.MainAxisAlignment.START
                ),
                width=600,
                height=600,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                padding=40
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            padding=40
        )
