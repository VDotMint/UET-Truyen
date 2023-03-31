"""_summary_
    """
from turtle import bgcolor

import flet as ft


class DetailView:
    """_summary_
    """

    def __init__(self):
        self.content = None
        self.create_content()

    def create_content(self):
        """
        iterate truyện
        """

        def items(count):
            items = []
            for i in range(1, count + 1):
                items.append(

                )
            return items

        detail_view = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Text(
                                        "Trang trủ",
                                        size=15,
                                        color="#288ad6",
                                    ),
                                    on_click=lambda e: print("Trang trủ clicked!"),
                                ),
                                ft.Icon(
                                    color="#288ad6",
                                    name=ft.icons.ARROW_RIGHT
                                ),
                                ft.Container(
                                    ft.Text(
                                        "Thể loại",
                                        size=15,
                                        color="#288ad6",
                                    ),
                                    on_click=lambda e: print("Thể loại clicked!"),
                                ),
                                ft.Icon(
                                    color="#288ad6",
                                    name=ft.icons.ARROW_RIGHT
                                ),
                                ft.Container(
                                    ft.Text(
                                        "Tên truyện",
                                        size=15,
                                        color="#288ad6",
                                    ),
                                    on_click=lambda e: print("Tên truyện clicked!"),
                                ),
                            ],
                        ),
                        padding=ft.padding.all(10),
                    ),
                    ft.Container(
                        ft.Text(
                            "Tên truyện",
                            color="#000000",
                            size=30
                        ),
                        margin=ft.margin.only(top=30)
                    ),
                    ft.Container(
                        ft.Text(
                            "[Cập nhật lúc: hh:mm dd/mm/yyyy]",
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
                                        src="assets/data/cover_img/100000.jpg",
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
                                                        "Chú tôi ở dị giới, Isekai Uncle, My Uncle in Another World, "
                                                        "Ojisan in Another World, 異世界おじさん",
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
                                                                    "Thể loại",
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
                                                        "2.370.684",
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
                                                        alignment=ft.alignment.center
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
                                                        alignment=ft.alignment.center
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
                            "Cô cam tâm tình nguyện làm một con rối của gia tộc, trở thành một sát thủ gián điệp, "
                            "nhưng cuối cùng cô lại phát hiện tất cả chỉ là trò lừa đảo mà gia tộc và đám đàn ông "
                            "dựng nên để lợi dụng cô! Sau khi rơi xuống biển chết đi, chính nhờ năng lượng Huyết Ngọc "
                            "Phượng Hoàng đã khiến cô sống lại trong thân xác của một cô gái có hoàn cảnh tương tự – "
                            "Cố Ninh. Để báo thù cho cả kiếp trước và kiếp này, cô quyết đoán trở về, bắt đầu gầy "
                            "dựng sự nghiệp riêng, kể từ đây, giới kinh doanh lại xuất hiện thêm một huyền thoại mới!",
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
            ft.Column(
                [
                    detail_view
                ],
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
        )
