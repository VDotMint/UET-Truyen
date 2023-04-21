"""_summary_
    """
import flet as ft
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.entity.comic_modules.comic_getter import ComicGetters
from src.theme.sub_theme.chapter_view import ChapterView
from src.theme.sub_theme.detail_view import DetailView


class Info(ft.Container):
    def __init__(self, app, id):
        super().__init__()
        self.app = app
        self.id = id
        self.max_chapter = ComicGetters.get_comic_chapter_count(self.id)

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
        self.content = ft.Column(
            [
                ft.Container(
                    ft.Image(
                        src=ComicImageModule.get_comic_cover_img_link(self.id),
                        width=250,
                        height=333
                    ),
                    width=250,
                    height=333,
                    bgcolor=ft.colors.WHITE,
                    on_click=self.detail,
                ),
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Text(
                                    ComicGetters.get_comic_name(self.id),
                                    size=15,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD
                                ),
                                on_click=self.detail,
                            ),
                            ft.Row(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "Chapters " + str(ComicGetters.get_comic_chapter_count(
                                                self.id)),
                                            # size=12,
                                            color=ft.colors.WHITE
                                        ),
                                        padding=5,

                                        on_click=self.read,
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            ComicGetters.get_comic_last_updated_delta(
                                                self.id, ComicGetters.get_comic_chapter_count(self.id)),
                                            # size=20,
                                            color=ft.colors.WHITE
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
                    bgcolor="#2b2b2b"
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            width=250,
        )


class Recommendation:
    """_summary_
    """

    def __init__(self, app):
        self.app = app
        self.content = None
        self.temp_comic_id_list = [100009, 100002, 100003, 100004, 100005]

        self.create_content()

    def create_content(self):
        """_summary_
        """

        def items(count, comic_list):
            items = []
            for i in range(count):
                items.append(Info(self.app, comic_list[i]))
            return items

        recommendation = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            "Truyện đề cử",
                            color="#2980b9",
                            size=30
                        ),

                        ft.Row(
                            items(5, self.temp_comic_id_list),
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                padding=5
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            margin=ft.margin.all(0),
            width=1450
        )
        self.content = ft.Container(
            recommendation,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            padding=20
        )
