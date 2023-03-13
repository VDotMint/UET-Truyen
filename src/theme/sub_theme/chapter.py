"""_summary_
    """
import os
import flet as ft


class Chapter:
    """_summary_
    """

    def __init__(self, path):
        self.name = "Vạn Cổ Tối Cường Tông"
        self.chapter = 1
        self.total_chapters = 20
        self.path = os.path.join(path, "assets/data/100000/1")

        self.images = os.listdir(self.path)
        self.images = [os.path.join(self.path, f) for f in self.images]

        self.content = None
        self.create_content()

    def create_content(self):
        """_summary_
        """
        image_display = ft.Container(
            ft.Column(
                [ft.Image(src=path) for path in self.images]
            ),
            alignment=ft.alignment.center,
        )

        info = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(value=self.name,
                                            color=ft.colors.BLUE, size=25),
                                    ft.Text("- Chapter " + str(self.chapter),
                                            color=ft.colors.BLACK, size=25)
                                ]

                            ),
                            padding=20
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Row(
                                        [ft.Text('Nếu không xem được truyện' +
                                                 'vui lòng đổi \"SERVER ẢNH\" bên dưới',
                                                 color=ft.colors.BLACK,
                                                 )],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(text="SERVER 1", bgcolor="#00cc66",
                                                              icon_color="#ffffff",
                                                              color="#ffffff"),
                                            ft.ElevatedButton(text="SERVER 2", bgcolor="#0099ff",
                                                              icon_color="#ffffff",
                                                              color="#ffffff"),
                                            ft.ElevatedButton(text="SERVER VIP", bgcolor="#0099ff",
                                                              icon_color="#ffffff",
                                                              color="#ffffff")
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(text="Báo lỗi", icon="warning",
                                                              bgcolor="#ff9933",
                                                              icon_color="#ffffff",
                                                              color="#ffffff")
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Container(
                                        ft.Row(
                                            [
                                                ft.Icon(name="info"),
                                                ft.Text(
                                                    value="Sử dụng mũi tên trái (←) hoặc phải (→)" +
                                                    " để chuyển chapter",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        bgcolor="#99ddff",
                                        padding=20,
                                    ),
                                    ft.Row(
                                        [
                                            ft.IconButton(
                                                icon="home", icon_color="#ff4d4d"),
                                            ft.IconButton(
                                                icon="list", icon_color="#ff4d4d"),
                                            ft.IconButton(
                                                icon="repeat", icon_color="#ff4d4d"),
                                            ft.ElevatedButton(
                                                text="<", color="#ffffff", bgcolor="#ff4d4d"),
                                            ft.Dropdown(
                                                width=300,
                                                options=[
                                                    ft.dropdown.Option(
                                                        "Chapter " + str(i))
                                                    for i in range(self.total_chapters, 0, -1)
                                                ],
                                                value="Chapter " +
                                                str(self.chapter),
                                                color="#000000",
                                                bgcolor="#ffffff",
                                            ),
                                            ft.ElevatedButton(
                                                text=">", color="#ffffff", bgcolor="#ff4d4d"),
                                            ft.ElevatedButton(
                                                text="Theo dõi", color="#ffffff", bgcolor="#00cc66")
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ]
                            ),
                            alignment=ft.alignment.center,
                            padding=20,
                            bgcolor=ft.colors.BLACK12
                        ),

                    ],

                ),
                width=900,
                bgcolor=ft.colors.WHITE
            ),
            alignment=ft.alignment.center
        )

        self.content = ft.Container(
            ft.Column(
                [
                    info,
                    image_display,
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK
        )
