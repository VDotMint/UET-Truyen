"""_summary_
    """
from turtle import bgcolor
from src.entity.comic import Comic
from src.entity.comic_modules.comic_query import ComicQuery
from src.entity.comic_modules.comic_getter import ComicGetters
from src.entity.comic_modules.comic_image_modules import ComicImageModule
import flet as ft

from src.theme.sub_theme.detail_view import DetailView


class Chapter(ft.Container):
    def __init__(self, app, info):
        super().__init__()

        self.app = app
        self.info = info
        self.max_chapter = ComicGetters.get_comic_chapter_count(self.info[0])
        self.name = ComicGetters.get_comic_name(self.info[0])
        # self.short_name =

        self.id = self.info[0]

        self.create_content()

    def detail(self, e):
        self.app.detail_page = DetailView(self.app, self.id)
        self.app.content.content.controls[2] = self.app.detail_page.content

        for x in self.app.navbar.tabs.controls:
            x.content.bgcolor = self.app.navbar.DEFAULT_COLOR

        self.app.navbar.tabs.controls[0].content.bgcolor = self.app.navbar.ACTIVE_COLOR

        self.app.content.update()

    def create_content(self):
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Image(
                            src=ComicImageModule.get_comic_cover_img_link(self.info[0]),
                            width=200,
                            height=266,
                        ),
                        on_click=self.detail,
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    ft.Text(
                                        self.name,
                                        color="#000000",
                                        size=15
                                    ),
                                    alignment=ft.alignment.center,
                                    on_click=self.detail,
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Row(
                                                [
                                                    ft.Container(
                                                        ft.Text(
                                                            "Chapter " + str(i),
                                                            size=12
                                                        ),
                                                        # padding=5,
                                                        on_click=lambda e: print("Chapter clicked!"),
                                                    ),
                                                    ft.Container(
                                                        ft.Text(
                                                            ComicGetters.get_comic_last_updated_delta(
                                                                self.info[0]),
                                                            size=12
                                                        ),
                                                        # padding=5,
                                                    ),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            )
                                        )
                                        for i in range(self.max_chapter, max(self.max_chapter - 3, 0), -1)
                                    ]
                                )
                            ],
                            spacing=20,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),

                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            ),
            width=200,
            height=420,
            bgcolor=ft.colors.WHITE
        )


class ListView:
    """_summary_
    """

    LATEST = 0
    HOT = 1

    def __init__(self, app, name, sort_type=LATEST):
        self.app = app
        self.name = name
        self.sort_type = sort_type

        self.recommendation = None
        self.content = None
        self.create_content()

    def change_name(self, name):
        self.name = name

        self.recommendation.content.content.controls[0].value = name
        self.content.update()



    def create_content(self):
        """_summary_
        """

        def items(count, recency_comic_list):
            items = []
            for i in range(count):
                current_comic_info = recency_comic_list[i]

                items.append(Chapter(self.app, current_comic_info))
            return items

        self.recommendation = ft.Container(
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
                    self.recommendation
                ]
            ),
            alignment=ft.alignment.center,
            # bgcolor=ft.colors.BLACK,
            width=1000,
            padding=40
        )
