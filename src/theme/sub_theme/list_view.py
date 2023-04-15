"""_summary_
    """
from turtle import bgcolor
from src.entity.comic import Comic
from src.entity.comic_modules.comic_query import ComicQuery
from src.entity.comic_modules.comic_getter import ComicGetters
from src.entity.comic_modules.comic_image_modules import ComicImageModule
import flet as ft


class ListView:
    """_summary_
    """

    LATEST = 0
    HOT = 1

    def __init__(self, name, sort_type=LATEST):
        self.name = name
        self.sort_type = sort_type

        self.content = None
        self.create_content()

    def create_content(self):
        """_summary_
        """
        def items(count, recency_comic_list):
            items = []
            for i in range(count):
                items.append(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Image(
                                    src=ComicImageModule.get_comic_cover_img_link(recency_comic_list[i][0])
                                ),
                                on_click=lambda e: print("Recommend clicked!"),
                            ),
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Text(
                                                ComicGetters.get_comic_name(recency_comic_list[i][0]),
                                                color="#000000",
                                                size=15
                                            ),
                                            on_click=lambda e: print("Title clicked!"),
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Chapter " + str(ComicGetters.get_comic_chapter_count(
                                                            recency_comic_list[i][0])),
                                                        size=12
                                                    ),
                                                    padding=5,
                                                    on_click=lambda e: print("Chapter clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        ComicGetters.get_comic_last_updated_delta(
                                                            recency_comic_list[i][0]),
                                                        size=12
                                                    ),
                                                    padding=5,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        )
                                    ],
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                bgcolor=ft.colors.WHITE
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        width=200,

                    )
                )
            return items

        recommendation = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            self.name,
                            color="#2980b9",
                            size=30
                        ),
                        ft.Row(
                            items(len(Comic.list_of_comics), ComicQuery.sort_comics_on_recency()),
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                            wrap=True,
                            width=1000
                        ),
                    ]
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            margin=ft.margin.all(0),
            width=1000
        )
        self.content = ft.Container(
            ft.Column(
                [
                    recommendation
                ]
            ),
            alignment=ft.alignment.center,
            # bgcolor=ft.colors.BLACK,
            width=1000,
            padding=40
        )
