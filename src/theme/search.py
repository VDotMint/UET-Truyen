import flet as ft

TYPES = [
"Action", "Adult", "Adventure", "Anime", "Chuyển Sinh", "Comedy", "Comic", "Cooking", "Cổ Đại", "Doujinshi", "Drama",
"Đam Mỹ", "Ecchi", "Fantasy", "Gender Bender", "Harem", "Lịch sử", "Horror", "Josei", "Live action", "Manga", "Manhua",
"Manhwa", "Martial Arts", "Mature", "Mecha", "Mystery", "Ngôn Tình", "One shot", "Psychological", "Romance",
"School Life", "Sci-fi", "Seinen", "Shoujo", "Shoujo Ai", "Shounen", "Shounen Ai", "Slice of Life", "Smut", "Soft Yaoi",
"Soft Yuri", "Sports", "Supernatural", "Thiếu Nhi", "Tragedy", "Trinh Thám", "Truyện Màu",
"Truyện scan", "Việt Nam", "Webtoon", "Xuyên Không", "Yaoi", "Yuri", "16+"
]

class SearchPage:
    def __init__(self):
        self.content = None
        self.types = None
        self.create_content()

    def create_content(self):

        def show_types(type_name: str):
            return ft.Checkbox(label=type_name, value=False, tristate=True)

        self.types = ft.GridView(
            [show_types(x) for x in TYPES],
            max_extent=180,
            runs_count=4,
            child_aspect_ratio=7,
        )

        chapter_nums_condition = [
            "> 0 chapter",
            ">= 50 chapter",
            ">= 100 chapter",
            ">= 200 chapter",
            ">= 500 chapter",
            ">= 1000 chapter"
        ]
        chapter_nums = ft.Row(
            [
                ft.Text(
                    "Số lượng chapter"
                ),
                ft.Dropdown(
                    width=250,
                    value=chapter_nums_condition[0],
                    options=[ft.dropdown.Option(x) for x in chapter_nums_condition]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        status_value = ["Tất cả", "Đang tiến hành", "Đã hoàn thành"]
        status = ft.Row(
            [
                ft.Text("Trang thái"),
                ft.Dropdown(
                    width=250,
                    value=status_value[0],
                    options=[ft.dropdown.Option(x) for x in status_value]
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        # Đối tượng
        subject_value = ["Tất cả", "Con gái", "Con trai"]
        subject = ft.Row(
            [
                ft.Text("Đối tượng"),
                ft.Dropdown(
                    width=250,
                    value=subject_value[0],
                    options=[ft.dropdown.Option(x) for x in subject_value]
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        sorted_type_value = ["Chapter mới", "Truyện mới", "Xem nhiều nhất", "Xem nhiều nhất tháng",
                             "Xem nhiều nhất tuần", "Xem nhiều nhất ngày", "Theo dõi nhiều nhất",
                             "Bình luận nhiều nhất", "Số chapter nhiều nhất"]
        sorted_type = ft.Row(
            [
                ft.Text("Sắp xếp theo"),
                ft.Dropdown(
                    width=250,
                    value=sorted_type_value[0],
                    options=[ft.dropdown.Option(x) for x in sorted_type_value]
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )


        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Card(
                                ft.Row(
                                    [
                                        ft.Text("Mẹo: Nếu bạn không thích thể loại Trung Quốc có thể bỏ check"),
                                        ft.Icon(ft.icons.INDETERMINATE_CHECK_BOX_SHARP),
                                        ft.Text("Manhua."),
                                        ft.Text("Nhấn 2 lần để bỏ check", color=ft.colors.RED)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                width=800,
                                height=60,
                            ),
                            width=900,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.WHITE,
                            padding=20
                        ),
                        ft.Container(
                            ft.Text(
                                "Tìm truyện nâng cao",
                                size=30,
                                color=ft.colors.BLUE
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Icon(ft.icons.CHECK_BOX_SHARP),
                                            ft.Text("Tìm trong những thể loại này")
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(ft.icons.INDETERMINATE_CHECK_BOX_SHARP),
                                            ft.Text("Loại trừ những thể loại này")
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(ft.icons.CHECK_BOX_OUTLINE_BLANK_SHARP),
                                            ft.Text("Truyện có thể thuộc hoặc không thuộc thể loại này")
                                        ]
                                    ),
                                ],
                                width=800,
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(
                                        "Thể loại",
                                        color=ft.colors.RED,
                                        size=25
                                    ),
                                    ft.FilledButton(
                                        "Reset",
                                        icon_color=ft.colors.BLUE,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=2),
                                        )
                                    )
                                ],
                                width=800,
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            ft.Container(
                                self.types,
                                width=800,
                                # height=600,
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.Container(
                                ft.GridView(
                                    [
                                        chapter_nums,
                                        status,
                                        subject,
                                        sorted_type
                                    ],
                                    max_extent=400,
                                    child_aspect_ratio=5.0,
                                ),
                                width=800,
                                # height=200,
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.FloatingActionButton(
                                "Tìm kiếm",
                                shape=ft.RoundedRectangleBorder(radius=2),
                                bgcolor="#ff9966",
                                width=200
                            ),
                            alignment=ft.alignment.center,
                            padding=40
                        )
                    ],
                ),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                width=900
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            padding=10
        )
