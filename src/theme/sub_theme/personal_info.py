import flet as ft

DEFAULT_COLOR = ft.colors.BLACK12
ACTIVE_COLOR = "#ff0066"

PINK_RED = "#ff0066"

class PersonalInfo:

    def __init__(self, app):
        self.app = app

        self.info = None
        self.tabs = None
        self.card = None
        self.content = None

        self.create_content()

    def create_content(self):
        self.info = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Text(
                            "Thông tin chung",
                            size=20,
                            weight=ft.FontWeight.BOLD
                        ),
                        padding=20
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Text("Thông tin tài khoản"),
                                ft.TextButton(
                                    "Chỉnh sửa",
                                    icon_color=ft.colors.BLUE,
                                    icon=ft.icons.EDIT
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        width=350,
                        # padding=
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text("Nguyên Anh"),
                                        ft.Text("Hóa thần"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.ProgressBar(height=20, value=40),
                                ft.Row(
                                    [
                                        ft.Text("Họ và tên"),
                                        ft.Text("Dajunctic Vu"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    [
                                        ft.Text("Email"),
                                        ft.Text("dajuncticvu@gmail.com"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    [
                                        ft.Text("Loại cấp bậc"),
                                        ft.Text("Tu tiên", color=ft.colors.RED),
                                        ft.TextButton(
                                            "Thay đổi",
                                            icon_color=ft.colors.BLUE,
                                            icon=ft.icons.CHANGE_CIRCLE
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ]
                        ),
                        width=350,
                        border=ft.border.only(
                            left=ft.border.BorderSide(color=PINK_RED, width=2),
                            right=ft.border.BorderSide(color=PINK_RED, width=2),
                            top=ft.border.BorderSide(color=PINK_RED, width=2),
                            bottom=ft.border.BorderSide(color=PINK_RED, width=2)
                        ),
                        padding=20
                    )
                ]
            )
        )

        self.tabs = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        # ft.TextButton("Thông tin chung", icon=ft.icons.BALLOT, icon_color=ACTIVE_COLOR,)
                        ft.Row(
                            [
                                ft.Icon(ft.icons.BALLOT, color=ACTIVE_COLOR),
                                ft.Text("Thông tin chung", color=ACTIVE_COLOR)
                            ]
                        ),
                        # bgcolor=ACTIVE_COLOR
                        # on_hover=lambda e: e.bgcolor=ft.colors.BLACK12
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.INFO),
                                ft.Text("Thông tin tài khoản")
                            ]
                        )
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.BOOK),
                                ft.Text("Truyện theo dõi")
                            ]
                        )
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.LIBRARY_BOOKS),
                                ft.Text("Truyện đã đăng")
                            ]
                        )
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.INSERT_COMMENT),
                                ft.Text("Bình luận")
                            ]
                        )
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.CIRCLE_NOTIFICATIONS),
                                ft.Text("Thông báo")
                            ]
                        )
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.PASSWORD),
                                ft.Text("Đổi mật khẩu")
                            ]
                        )
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(ft.icons.EXIT_TO_APP),
                                ft.Text("Thoát")
                            ]
                        )
                    ),
                ]
            ),
            width=300,
            bgcolor=ft.colors.BLACK12,
            padding=20
        )

        self.card = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Card(
                                    ft.Row(
                                        [
                                            ft.Container(
                                                ft.Image(
                                                    "assets/gui/avatar.jpg",
                                                    width=80,
                                                ),
                                                padding=20
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Text("Tài khoản của: ", color="#000000"),
                                                        ft.Text(
                                                            "Dajunctic Vu",
                                                            color="#000000",
                                                            weight=ft.FontWeight.BOLD
                                                        )
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER
                                                ),
                                                # width=180,
                                                alignment=ft.alignment.center,
                                                # padding=20,
                                                # bgcolor=ft.colors.RED
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.START
                                    ),
                                    height=120,
                                    width=300
                                ),
                                self.tabs
                            ]
                        ),
                        width=270,
                    ),
                    ft.VerticalDivider(color=ft.colors.BLUE, width=100),
                    self.info
                ],
                spacing=10
            ),
            width=1000,
            height=500,
            bgcolor=ft.colors.WHITE,
            padding=30
        )
        self.content = ft.Container(
            self.card,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            padding=20
        )
