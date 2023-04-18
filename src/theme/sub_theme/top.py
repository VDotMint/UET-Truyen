"""_summary_
    """
import flet as ft
from src.entity.comic_modules.comic_getter import ComicGetters
from src.entity.comic_modules.comic_ranking import ComicRanking
from src.entity.comic_modules.comic_image_modules import ComicImageModule
from src.theme.sub_theme.extra import SmallCard, CardType

ACTIVE_BG_COLOR = "#ffffff"
BG_COLOR = "#CCCCCC"
BORDER_COLOR = "#C0C0C0"
ACTIVE_BORDER_COLOR = "#33cccc"


class Top:
    """_summary_
    """

    def __init__(self, app):
        self.app = app
        self.list_display = None
        self.content = None
        self.tabs = None

        self.monthly_rank_list = ComicRanking.get_view_count_ranking_by_time("monthly", 10)
        self.weekly_rank_list = ComicRanking.get_view_count_ranking_by_time("weekly", 10)
        self.daily_rank_list = ComicRanking.get_view_count_ranking_by_time("daily", 10)

        self.create_content()

    def create_content(self):
        """
        iterate truyện
        """

        def items(count, top_comic_list):
            items = []
            for i in range(count):
                items.append(
                    SmallCard(self.app, identy=top_comic_list[i][0], view_info=top_comic_list[i][1], card_type=CardType.TOP, order=i + 1)
                )
            return items

        def change_top(e: ft.ContainerTapEvent):
            for x in self.tabs.controls:
                x.bgcolor = BG_COLOR

            e.control.bgcolor = ACTIVE_BG_COLOR

            if e.control.content.value == "Top Tháng":
                self.list_display.content.controls = items(6, self.monthly_rank_list)
            elif e.control.content.value == "Top Tuần":
                self.list_display.content.controls = items(6, self.weekly_rank_list)
            elif e.control.content.value == "Top Ngày":
                self.list_display.content.controls = items(6, self.daily_rank_list)

            self.list_display.update()

            self.tabs.update()

        self.tabs = ft.Row(
            [
                ft.Container(
                    ft.Text(
                        "Top Tháng",
                        color="#000000",
                        size=15
                    ),
                    border=ft.border.only(
                        left=ft.border.BorderSide(1, "#C0C0C0"),
                        bottom=ft.border.BorderSide(1, "#C0C0C0"),
                        top=ft.border.BorderSide(1, BORDER_COLOR)
                    ),
                    bgcolor=ACTIVE_BG_COLOR,
                    width=97,
                    height=50,
                    alignment=ft.alignment.center,
                    on_click=change_top,
                ),
                ft.Container(
                    ft.Text(
                        "Top Tuần",
                        color="#000000",
                        size=15
                    ),
                    border=ft.border.only(
                        left=ft.border.BorderSide(1, "#C0C0C0"),
                        bottom=ft.border.BorderSide(1, "#C0C0C0"),
                        top=ft.border.BorderSide(1, BORDER_COLOR),
                    ),
                    bgcolor=BG_COLOR,
                    width=97,
                    height=50,
                    alignment=ft.alignment.center,
                    on_click=change_top,
                ),
                ft.Container(
                    ft.Text(
                        "Top Ngày",
                        color="#000000",
                        size=15
                    ),
                    border=ft.border.only(
                        left=ft.border.BorderSide(1, "#C0C0C0"),
                        right=ft.border.BorderSide(1, "#C0C0C0"),
                        bottom=ft.border.BorderSide(1, "#C0C0C0"),
                        top=ft.border.BorderSide(1, BORDER_COLOR),
                    ),
                    bgcolor=BG_COLOR,
                    width=96,
                    height=50,
                    alignment=ft.alignment.center,
                    on_click=change_top,
                )
            ],
            spacing=0
        )

        self.list_display = ft.Container(
            ft.Column(
                items(6, self.monthly_rank_list),
                spacing=0
            ),
        )

        top = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            self.tabs,
                            height=50,
                            width=300,
                        ),
                        self.list_display

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
                    top
                ],
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK,
            width=300,
        )
