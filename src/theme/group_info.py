from typing import List

import flet as ft


class GroupInfo:
    def __init__(self):
        self.content = None
        self.create_content()

    def create_content(self):
        def member_info(name: str, nickname: List[str], img_url: str, class_name: str):
            return ft.Card(
                content=ft.Container(
                    ft.Column(
                        [
                            ft.Container(
                                ft.CircleAvatar(
                                    foreground_image_url=img_url,
                                    width=200,
                                    height=200,
                                ),
                                alignment=ft.alignment.center
                            ),
                            ft.ListTile(
                                # leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text(name),
                                subtitle=ft.Text(
                                    ", ".join(nickname)
                                ),
                            ),
                            ft.ListTile(
                                # leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text(class_name),
                                subtitle=ft.Text(
                                    "Đại học công nghệ - ĐHQG Hà Nội"
                                ),
                            ),
                        ],
                    )
                ),
                width=280,
                height=380
            )

        member_list = [
            member_info("Vũ Quý Đạt", ["dajunctic"],
                        "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/321732529_605676428232150_324037283300"
                        "1934045_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=EZffhltV-z8AX_DSqKt&_nc_ht=scon"
                        "tent.fhan3-2.fna&oh=00_AfBLjWAoYq9MDA43cQ6MCixoMBlztnq6Tzwnr4FZXEURJw&oe=6439A645"
                        , "K66 CA-CLC1"),
            member_info("Lê Vũ Minh", ["VDotMint"],
                        "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-1/279293120_1383311835474813_64518851945"
                        "61106848_n.jpg?stp=dst-jpg_s320x320&_nc_cat=111&ccb=1-7&_nc_sid=7206a8&_nc_ohc=js08d_C3iIQA"
                        "X8TUuUX&_nc_ht=scontent.fhan3-2.fna&oh=00_AfADV4H_7oOE81RBCpMbsV7bMUD7HeShqcokP2Xd2vLKbA&oe"
                        "=643B5AEB", "K66 CA-CLC1"),
            member_info("Ngô Danh Lam", ["Lam NDL"],
                        "https://scontent.fhan3-1.fna.fbcdn.net/v/t39.30808-1/328439091_967496651178801_67465184751579"
                        "76491_n.jpg?stp=c8.4.312.312a_dst-jpg_p320x320&_nc_cat=110&ccb=1-7&_nc_sid=7206a8&_nc_ohc=jx3"
                        "iNre9esAAX__Yaqb&_nc_ht=scontent.fhan3-1.fna&oh=00_AfCiWj9NRQxJ-Qq05D_xi6V1YYl-JwzcbaAOQDy7"
                        "ogZlbw&oe=643ACF1A", "K66 CA-CLC1"),
            member_info("Phạm Hoàng Ân", ["anhensam"],
                        "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-1/324030406_2084395011752604_8451143775804"
                        "184435_n.jpg?stp=dst-jpg_s320x320&_nc_cat=100&ccb=1-7&_nc_sid=7206a8&_nc_ohc=u6zqjrAcgwoAX9Zr"
                        "PAf&_nc_ht=scontent.fhan3-2.fna&oh=00_AfCsyMKbWhgUQ9pdxG5eL4U_k2Jx8MmxrG9ZqU3vmFjMdQ&oe=6439D"
                        "94A", "K66 CA-CLC3"),
            member_info("Nguyễn Tuấn Hưng", ["Hưng Fake"],
                        "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-1/334015963_585802306770342_25113446128138"
                        "40534_n.jpg?stp=dst-jpg_s320x320&_nc_cat=103&ccb=1-7&_nc_sid=7206a8&_nc_ohc=08h4E-S-CwAAX9u3a"
                        "9k&_nc_ht=scontent.fhan3-2.fna&oh=00_AfC9bRi-XSRNP9TRzyMn9i9ZiBhO_123kZ5xZ3wDDfIiaA&oe=643B28"
                        "25", "K66 CA-CLC1")
        ]

        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Divider(),
                        ft.Container(
                            ft.Text(
                                "Các thành viên trong nhóm UET Sentai",
                                color=ft.colors.RED,
                                size=30,
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Divider(),
                        ft.Container(
                            ft.Row(
                                member_list[:3],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.Row(
                                member_list[3:],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            alignment=ft.alignment.center
                        )
                    ],
                    spacing=20,
                    width=840,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=20,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                width=1000
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12
        )
