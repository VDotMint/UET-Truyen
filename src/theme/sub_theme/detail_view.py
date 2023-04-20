"""_summary_
    """
from turtle import bgcolor

import flet as ft

from src.entity.comic_modules.comic_getter import ComicGetters
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.theme.sub_theme.chapter_view import ChapterView


class DetailView:
    """_summary_
    """

    def __init__(self, app, id):
        self.app = app
        self.id = id

        self.name = ComicGetters.get_comic_name(self.id)
        self.max_chapter = ComicGetters.get_comic_chapter_count(self.id)
        self.date = ComicGetters.get_comic_last_updated_date(self.id)
        self.intro_content = ComicGetters.get_comic_content(self.id)


        self.view_count = ComicGetters.get_comic_view_count(self.id)

        self.content = None
        self.create_content()

    def read(self, e):
        chapter = 0

        if e.control.content.value == "Đọc mới nhất":
            chapter = self.max_chapter
        elif e.control.content.value == "Đọc từ đầu":
            chapter = 1
        else:
            chapter = int(e.control.content.value.split(' ')[1])

        self.app.chapter_page = ChapterView(self.app, self.id, chapter)
        self.app.content.content.controls[2] = self.app.chapter_page.content

        self.app.content.update()

    def create_content(self):
        """
        iterate truyện
        """

        self.chapter_list = [
            ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            ft.Text("Chapter " + str(i)),
                            on_click=self.read
                        ),
                        ft.Text(ComicGetters.get_comic_last_updated_delta(self.id, i)),
                        ft.Text(ComicGetters.get_chapter_view_count(self.id, i)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                # padding=20
                # bgcolor=ft.colors.BLACK12
            )
            for i in range(self.max_chapter, 0, -1)
        ]


        detail_view = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Text(
                            self.name,
                            color="#000000",
                            size=30
                        ),
                        margin=ft.margin.only(top=30)
                    ),
                    ft.Container(
                        ft.Text(
                            f"[Cập nhật lúc: {self.date}]",
                            color="#777676",
                            size=15
                        ),
                        margin=ft.margin.only(bottom=20)
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Image(
                                        src=ComicImageModule.get_comic_cover_img_link(self.id),
                                        width=230
                                    ),
                                    margin=ft.margin.only(right=20)
                                ),
                                ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Tên khác",
                                                        color="#777676",
                                                        size=15
                                                    ),
                                                    width=80,
                                                    margin=ft.margin.only(right=20)
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        ComicGetters.get_comic_name(self.id),
                                                        color="#777676",
                                                        size=15
                                                    ),
                                                    width=250
                                                ),
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Tác giả",
                                                        color="#777676",
                                                        size=15
                                                    ),
                                                    width=80,
                                                    margin=ft.margin.only(right=20)
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Tên tác giả",
                                                        color="#288ad6",
                                                        size=15
                                                    ),
                                                    on_click=lambda e: print("Tên tác giả clicked!"),
                                                )
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Tình trạng",
                                                        color="#777676",
                                                        size=15
                                                    ),
                                                    width=80,
                                                    margin=ft.margin.only(right=20)
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        "Đang tiến hành",
                                                        color="#777676",
                                                        size=15
                                                    )
                                                ),
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Thể loại",
                                                        color="#777676",
                                                        size=15
                                                    ),
                                                    width=80,
                                                    margin=ft.margin.only(right=20)
                                                ),
                                                ft.Container(
                                                    ft.Row(
                                                        [
                                                            ft.Container(
                                                                ft.Text(
                                                                    ", ".join(ComicGetters.get_comic_type(self.id)),
                                                                    color="#288ad6",
                                                                    size=15
                                                                ),
                                                                on_click=lambda e: print("Thể loại clicked!"),
                                                            )
                                                        ],
                                                        wrap=True,
                                                        width=200
                                                    )
                                                ),
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    ft.Text(
                                                        "Lượt xem",
                                                        color="#777676",
                                                        size=15
                                                    ),
                                                    width=80,
                                                    margin=ft.margin.only(right=20)
                                                ),
                                                ft.Container(
                                                    ft.Text(
                                                        self.view_count,
                                                        color="#777676",
                                                        size=15
                                                    )
                                                ),
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                                        ft.Row(
                                            [
                                                ft.ElevatedButton(
                                                    content=ft.Container(
                                                        ft.Text(
                                                            "Theo dõi",
                                                            color="#ffffff",
                                                            size=15
                                                        ),
                                                        width=80,
                                                        alignment=ft.alignment.center
                                                    ),
                                                    bgcolor="#5cb85c"
                                                ),
                                                ft.Text(
                                                    "22.076",
                                                    weight=ft.FontWeight.BOLD,
                                                    size=15,
                                                    color="#000000"
                                                ),
                                                ft.Text(
                                                    "Lượt theo dõi",
                                                    size=15,
                                                    color="#000000"
                                                )
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            [
                                                ft.ElevatedButton(
                                                    content=ft.Container(
                                                        ft.Text(
                                                            "Đọc từ đầu",
                                                            color="#ffffff",
                                                            size=15
                                                        ),
                                                        width=80,
                                                        alignment=ft.alignment.center,
                                                        on_click=self.read
                                                    ),
                                                    bgcolor="#f0ad4e"
                                                ),
                                                ft.ElevatedButton(
                                                    content=ft.Container(
                                                        ft.Text(
                                                            "Đọc mới nhất",
                                                            color="#ffffff",
                                                            size=15
                                                        ),
                                                        width=100,
                                                        alignment=ft.alignment.center,
                                                        on_click=self.read
                                                    ),
                                                    bgcolor="#f0ad4e"
                                                ),
                                            ],
                                            vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                                    ]
                                )
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                        padding=ft.padding.all(15)
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(
                                    name=ft.icons.INSERT_DRIVE_FILE_OUTLINED,
                                    color="#288ad6",
                                    size=17
                                ),
                                ft.Text(
                                    "NỘI DUNG",
                                    color="#288ad6",
                                    size=17
                                )
                            ]
                        ),
                        padding=ft.padding.all(5),
                        margin=ft.margin.only(top=20)
                    ),
                    ft.Divider(
                        color="#288ad6",
                        thickness=2,
                        height=2
                    ),
                    ft.Container(
                        ft.Text(
                            self.intro_content,
                            size=15,
                            color="#000000"
                        ),
                        padding=ft.padding.all(5),
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Icon(
                                    name=ft.icons.FORMAT_LIST_BULLETED,
                                    color="#288ad6",
                                    size=17
                                ),
                                ft.Text(
                                    "DANH SÁCH CHƯƠNG",
                                    color="#288ad6",
                                    size=17
                                )
                            ]
                        ),
                        margin=ft.margin.only(top=20),
                        padding=ft.padding.all(5),
                    ),
                    ft.Divider(
                        color="#288ad6",
                        thickness=2,
                        height=2
                    ),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Text(
                                    "Số chương",
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Cập nhật",
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Lượt xem",
                                    weight=ft.FontWeight.BOLD
                                ),

                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        padding=10
                    ),

                    ft.Container(
                        ft.Column(
                            self.chapter_list
                        ),
                        alignment=ft.alignment.top_left,
                        padding=10
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            margin=ft.margin.all(0),
            width=700
        )
        self.content = ft.Container(
            detail_view,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            padding=30
        )
