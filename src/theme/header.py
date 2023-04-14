"""_summary_
    """
import flet as ft


class Header:
    """_summary_
    """

    def __init__(self, app):
        self.app = app

        self.login_button = None
        self.account_header = None
        self.content = None
        self.create_content()

    def create_content(self):
        """_summary_
        """
        def active_home():
            for x in self.app.navbar.tabs.controls:
                x.content.bgcolor = self.app.navbar.DEFAULT_COLOR

            self.app.navbar.tabs.controls[0].content.bgcolor = self.app.navbar.ACTIVE_COLOR

            self.app.content.update()

        # ############## Vào trang để đăng nhập hoặc đăng ký ###########
        def change_page(e: ft.ContainerTapEvent):
            if e.control.text == "Đăng nhập":
                self.app.content.content.controls[2] = self.app.login.content
            elif e.control.text == "Đăng ký":
                self.app.content.content.controls[2] = self.app.signup.content

            active_home()

        def to_personal_info(e: ft.ContainerTapEvent):
            self.app.content.content.controls[2] = self.app.personal_info.content
            # self.app.personal_info.update()

            if e.control.content.controls[1].value == "Trang cá nhân":
                pass
            elif e.control.content.controls[1].value == "Truyện theo dõi":
                pass

            active_home()

        self.login_button = ft.Container(
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Đăng ký",
                        color="#ffffff",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=2)
                        ),
                        bgcolor="#ff9966",
                        width=120,
                        on_click=change_page
                    ),
                    ft.ElevatedButton(
                        text="Đăng nhập",
                        color="#ffffff",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=2)
                        ),
                        bgcolor="#ff9966",
                        width=120,
                        on_click=change_page
                    ),
                ],
            ),
            padding=2
        )

        self.account_header = ft.Container(
            ft.PopupMenuButton(
                content=ft.Row(
                    [
                        ft.Text(
                            "Dajunctic Vu",
                            # size=20,
                            color=ft.colors.ORANGE,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Icon(ft.icons.ARROW_DROP_DOWN, color=ft.colors.ORANGE),
                    ]
                ),
                # icon=ft.icons.ARROW_DROP_DOWN,
                items=[
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.INFO),
                                ft.Text("Trang cá nhân"),
                            ]
                        ),
                        on_click=to_personal_info
                    ),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.BOOK),
                                ft.Text("Truyện theo dõi"),
                            ]
                        ),
                        on_click=to_personal_info
                    ),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.EXIT_TO_APP),
                                ft.Text("Thoát"),
                            ]
                        ),
                        on_click=self.app.sign_out
                    ),
                ]
            ),
            padding=10
        )

        self.content = ft.Container(
            ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            ft.Image("assets/icons/loading-animation.png"),
                            padding=ft.padding.only(right=50)
                        ),
                        ft.Container(
                            ft.TextField(
                                hint_text="Tìm truyện...",
                                bgcolor="#ffffff",
                                color=ft.colors.BLACK,
                                border_color="#ffffff",
                                selection_color="#ffffff",
                                filled=True,

                            )
                        ),
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.SEARCH,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2)
                                ),
                                icon_color="#ffffff"
                            ),
                        ),
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.LIGHTBULB,
                                icon_color="#ffffff"
                            ),
                            padding=ft.padding.only(left=30)
                        ),
                        ft.Container(
                            ft.IconButton(
                                icon=ft.icons.COMMENT,
                                icon_color="#ffffff"
                            ),
                        ),
                        self.login_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                    # width=1000
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor="#007a99",
            height=50,
            margin=ft.margin.all(0)
        )

