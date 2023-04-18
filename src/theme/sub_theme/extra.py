from enum import Enum

import flet as ft

from src.entity.comic_modules.comic_getter import ComicGetters
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.theme.sub_theme.chapter_view import ChapterView
from src.theme.sub_theme.detail_view import DetailView


class CardType(Enum):
    NORMAL = 1,
    TOP = 2


def short_name(name, card_type=CardType.NORMAL):
    max_width = 26 if card_type == CardType.NORMAL else 22
    if len(name) > max_width:
        return name[0:max_width] + "..."
    return name

class SmallCard(ft.Container):
    def __init__(self, app, identy, view_info="", card_type=CardType.NORMAL, order=-1):
        super().__init__()

        self.app = app
        self.id = identy
        self.max_chapter = ComicGetters.get_comic_chapter_count(self.id)
        self.name = ComicGetters.get_comic_name(self.id),
        self.name = "".join(self.name)
        self.short_name = short_name(self.name, card_type)

        self.view_info = view_info

        self.card_type = card_type
        self.order = order

        self.create_content()

    def detail(self, e):
        self.app.detail_page = DetailView(self.app, self.id)
        self.app.content.content.controls[2] = self.app.detail_page.content

        for x in self.app.navbar.tabs.controls:
            x.content.bgcolor = self.app.navbar.DEFAULT_COLOR

        self.app.navbar.tabs.controls[0].content.bgcolor = self.app.navbar.ACTIVE_COLOR

        self.app.content.update()

    def read(self, e):
        self.app.chapter_page = ChapterView(self.app, self.id, self.max_chapter)
        self.app.content.content.controls[2] = self.app.chapter_page.content

        for x in self.app.navbar.tabs.controls:
            x.content.bgcolor = self.app.navbar.DEFAULT_COLOR

        self.app.navbar.tabs.controls[0].content.bgcolor = self.app.navbar.ACTIVE_COLOR

        self.app.content.update()

    def create_content(self):

        if self.card_type == CardType.NORMAL:
            self.content = ft.Container(
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Image(
                                        src=ComicImageModule.get_comic_cover_img_link(self.id),
                                    ),
                                    on_click=self.detail,
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Text(
                                                self.short_name,
                                                size=15,
                                                color="#000000",
                                            ),
                                            on_click=self.detail,
                                        ),
                                        ft.Container(
                                            ft.Row(
                                                [
                                                    ft.Container(
                                                        ft.Text(
                                                            "Chapters " + str(self.max_chapter),
                                                            size=15,
                                                            color="#000000",
                                                        ),
                                                        on_click=self.read,
                                                    ),
                                                    ft.Container(
                                                        ft.Text(
                                                            ComicGetters.get_comic_last_updated_delta(self.id),
                                                            size=10,
                                                            color="#C0C0C0"
                                                        ),
                                                    ),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                width=220
                                            ),

                                        ),
                                        ft.Container(
                                            ft.Text(
                                                "Đọc tiếp Chapter xx",
                                                size=10,
                                                color=ft.colors.BLACK54,
                                            ),
                                            on_click=self.read,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                                ),
                            ]
                        ),

                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                border=ft.border.only(
                    left=ft.border.BorderSide(1,"#C0C0C0"),
                    right=ft.border.BorderSide(1, "#C0C0C0"),
                    bottom=ft.border.BorderSide(1, "#C0C0C0")
                ),
                height=80,
                width=300,
                padding=10
            )

        elif self.card_type == CardType.TOP:
            self.content = ft.Container(
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    "0" + str(self.order),
                                    color="#2980b9",
                                    size=20,
                                ),
                                ft.Container(
                                    ft.Image(
                                        src=ComicImageModule.get_comic_cover_img_link(self.id)
                                    ),
                                    on_click=lambda e: print("Cover truyen clicked!"),
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Text(
                                                self.short_name,
                                                size=15,
                                                color="#000000",
                                            ),
                                            on_click=lambda e: print("Tên truyện clicked!"),
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Chapter " + str(self.max_chapter),
                                                        size=15,
                                                        color="#000000",
                                                    ),
                                                    on_click=lambda e: print("Chapter clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Row(
                                                        [
                                                            ft.Icon(
                                                                name=ft.icons.REMOVE_RED_EYE,
                                                                color="#C0C0C0",
                                                                size=12
                                                            ),
                                                            ft.Text(
                                                                self.view_info,
                                                                color="#C0C0C0",
                                                                size=15
                                                            ),
                                                        ],
                                                        spacing=0,
                                                    )
                                                )
                                            ],
                                            width=180,
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                                ),
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                border=ft.border.only(
                    left=ft.border.BorderSide(1, "#C0C0C0"),
                    right=ft.border.BorderSide(1, "#C0C0C0"),
                    bottom=ft.border.BorderSide(1, "#C0C0C0")
                ),
                height=80,
                width=300,
                padding=10
            )

