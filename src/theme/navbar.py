"""_summary_
    """
import flet as ft

# ACTIVE_TEXT_COLOR = "#00ccff"

class NavBar:
    """_summary_
    """
    ACTIVE_COLOR = "#ffffff"
    DEFAULT_COLOR = "#e0e0eb"

    def __init__(self, app):
        self.app = app
        self.tabs = None
        self.navbar = None
        self.content = None
        self.create_content()

    def create_content(self):
        """_summary_
        """
        def change_page(e: ft.ContainerTapEvent):
            for x in self.tabs.controls:
                x.content.bgcolor = self.DEFAULT_COLOR

            e.control.bgcolor = self.ACTIVE_COLOR
            # print(e.control.text)

            if e.control.text == "TRANG CHỦ":
                self.app.content.content.controls[2] = self.app.home.content
            elif e.control.text == "HOT":
                self.app.content.content.controls[2] = self.app.hot.content
            elif e.control.text == "THEO DÕI":
                self.app.content.content.controls[2] = self.app.following_page.content
            elif e.control.text == "LỊCH SỬ":
                self.app.content.content.controls[2] = self.app.history_page.content
            elif e.control.text == "TẢI APP":
                self.app.content.content.controls[2] = self.app.app_download_page.content
            elif e.control.text == "GROUP":
                self.app.content.content.controls[2] = self.app.group_info_page.content
            elif e.control.text == "TÌM TRUYỆN":
                self.app.content.content.controls[2] = self.app.search_page.content

            self.tabs.update()
            self.app.content.update()

        self.tabs = ft.Row(
            [
                ft.Container(
                    ft.FloatingActionButton(
                        text="TRANG CHỦ",
                        icon=ft.icons.HOUSE,
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.ACTIVE_COLOR,
                        on_click=change_page
                    )
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="HOT",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page
                    )
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="THEO DÕI",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page
                    )
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="LỊCH SỬ",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page
                    )
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="THỂ LOẠI",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page,
                    ),
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="XẾP HẠNG",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        on_click=change_page,
                        width=100,
                    ),
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="TÌM TRUYỆN",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page
                    )
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="TẢI APP",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page
                    )
                ),
                ft.Container(
                    ft.FloatingActionButton(
                        text="GROUP",
                        shape=ft.RoundedRectangleBorder(radius=2),
                        bgcolor=self.DEFAULT_COLOR,
                        width=100,
                        on_click=change_page
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        )

        self.navbar = ft.Container(
            ft.Container(
                self.tabs,
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            height=50,
            margin=ft.margin.all(0)
        )

        self.content = ft.Container(
            ft.Column(
                [
                    self.navbar
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor="#f0f0f5"
        )
