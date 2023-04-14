import flet as ft


class AppDownload:
    def __init__(self):
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Text(
                            "Hiện tại nhóm mình chưa build xong app! Mong các bạn thông cảm!",
                            size=25,
                            color=ft.colors.RED
                        ),
                        alignment=ft.alignment.center,
                        padding=0
                    ),
                    ft.Container(
                        ft.Image(src="assets/gui/building.gif"),
                        alignment=ft.alignment.center
                    )
                ]
            ),
            padding=30
        )
