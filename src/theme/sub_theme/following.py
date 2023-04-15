"""_summary_
    """
from turtle import bgcolor
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.entity.comic_modules.comic_getter import ComicGetters
import flet as ft


class Following:
    """_summary_
    """

    def __init__(self):
        self.content = None
        self.following_list = [100004, 100008, 100005, 100006]

        self.create_content()

    def create_content(self):
        """
        iterate truyện
        """
        def items(count, comic_list):
            items = []
            for i in range(count):
                items.append(
                    ft.Container(
                        ft.Row(
                            [
                                ft.Row(
                                    [
                                        ft.Container(
                                            ft.Image(
                                                src=ComicImageModule.get_comic_cover_img_link(comic_list[i]),
                                            ),
                                            on_click=lambda e: print("Cover truyen clicked!"),
                                        ),
                                        ft.Column(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        ComicGetters.get_comic_name(comic_list[i]),
                                                        size=15,
                                                        color="#000000",
                                                    ),
                                                    on_click=lambda e: print("Tên truyện clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Chapters " + str(ComicGetters.get_comic_chapter_count(
                                                            comic_list[i])),
                                                        size=15,
                                                        color="#000000",
                                                    ),
                                                    on_click=lambda e: print("Chapter clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Đọc tiếp Chapter xx",
                                                        size=10,
                                                        color=ft.colors.BLACK54,
                                                    ),
                                                    on_click=lambda e: print("Đọc tiếp clicked!"),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND
                                        ),
                                    ]
                                ),
                                ft.Text(
                                    ComicGetters.get_comic_last_updated_delta(comic_list[i]),
                                    size=10,
                                    color="#C0C0C0"
                                )
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
                )
            return items

        following = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(
                                        "Truyện đang theo dõi",
                                        color="#2980b9",
                                        size=20
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            "Xem tất cả",
                                            color="#000000",
                                            size=10
                                        ),
                                        on_click=lambda e: print("Xem tất cả clicked!"),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND
                            ),
                            height=50,
                            width=300,
                            border=ft.border.all(1,"#C0C0C0")
                        ),
                        ft.Column(
                            items(len(self.following_list), self.following_list),
                            spacing=0
                        ),
                    ],
                    spacing=0
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            margin=ft.margin.all(0)
        )
        self.content = ft.Container(
            ft.Column(
                [
                    following
                ],
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
            width=300,
        )
