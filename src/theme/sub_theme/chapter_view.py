"""_summary_
    """
import os
import flet as ft

from src.entity.comic_modules.comic_getter import ComicGetters
from src.entity.comic_modules.comic_image_modules import ComicImageModule


class ChapterView:
    """_summary_
    """

    def __init__(self, app, id, chapter=1):
        self.app = app
        self.id = id
        self.chapter = chapter
        self.dropdown = None
        self.name = ComicGetters.get_comic_name(id)

        self.total_chapters = ComicGetters.get_comic_chapter_count(id)

        self.images = ComicImageModule.get_comic_content_images(self.id, self.chapter)

        self.content = None
        self.create_content()

    def dec(self, e):
        self.chapter = 1 + (self.chapter - 1 + self.total_chapters - 1) % self.total_chapters
        self.dropdown.content.value = "Chapter " + str(self.chapter)
        self.read(e, False)

    def inc(self, e):
        self.chapter = 1 + (self.chapter - 1 + self.total_chapters + 1) % self.total_chapters
        self.dropdown.content.value = "Chapter " + str(self.chapter)
        self.read(e, False)

    def read(self, e, flag=True):
        if flag:
            self.chapter = int(e.control.value.split(' ')[1])

        self.app.chapter_page = ChapterView(self.app, self.id, self.chapter)
        self.app.content.content.controls[2] = self.app.chapter_page.content

        for x in self.app.navbar.tabs.controls:
            x.content.bgcolor = self.app.navbar.DEFAULT_COLOR

        self.app.navbar.tabs.controls[0].content.bgcolor = self.app.navbar.ACTIVE_COLOR

        self.app.content.update()

    def create_content(self):
        """_summary_
        """
        image_display = ft.Container(
            ft.Column(
                [ft.Image(src=path) for path in self.images],
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK
        )

        self.dropdown = ft.Container(
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
                on_change=self.read
            ),
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
                            ft.Divider()
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
                                                text="<", color="#ffffff", bgcolor="#ff4d4d", on_click=self.dec),
                                            self.dropdown,
                                            ft.ElevatedButton(
                                                text=">", color="#ffffff", bgcolor="#ff4d4d", on_click=self.inc),
                                            ft.ElevatedButton(
                                                text="Theo dõi", color="#ffffff", bgcolor="#00cc66")
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ]
                            ),
                            alignment=ft.alignment.center,
                            padding=20,
                            bgcolor=ft.colors.WHITE
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
            bgcolor=ft.colors.BLACK12
        )
