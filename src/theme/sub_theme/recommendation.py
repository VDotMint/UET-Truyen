"""_summary_
    """
import flet as ft
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.entity.comic_modules.comic_getter import ComicGetters


# class Info(ft.C)

class Recommendation:
    """_summary_
    """

    def __init__(self):
        self.content = None
        self.temp_comic_id_list = [100009, 100002, 100003, 100004, 100005]

        self.create_content()

    def create_content(self):
        """_summary_
        """
        def items(count, comic_list):
            items = []
            for i in range(count):
                items.append(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Image(
                                    src=ComicImageModule.get_comic_cover_img_link(comic_list[i]),
                                    width=250,
                                    height=333
                                ),
                                width=250,
                                height=333,
                                bgcolor=ft.colors.WHITE,
                                on_click=lambda e: print("Recommend clicked!"),
                            ),
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Text(
                                                ComicGetters.get_comic_name(comic_list[i]),
                                                size=15
                                            ),
                                            on_click=lambda e: print("Title clicked!"),
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Chapters " + str(ComicGetters.get_comic_chapter_count(
                                                            comic_list[i])),
                                                        # size=12,
                                                        color=ft.colors.WHITE
                                                    ),
                                                    padding=5,

                                                    on_click=lambda e: print("Chapter clicked!"),
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        ComicGetters.get_comic_last_updated_delta(comic_list[i]),
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
                                bgcolor=ft.colors.BLACK
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        width=250,
                    )
                )
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
            ft.Column(
                [
                    recommendation
                ]
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            padding=20
            # width=1250,
            # height=333
        )
