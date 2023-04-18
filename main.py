"""_summary_
    """
import flet as ft
from settings import TITLE
from src.entity.comic import Comic
from src.theme.app_download import AppDownload
from src.theme.filter import FilterPage
from src.theme.following_page import FollowingPage
from src.theme.footer import *
from src.theme.group_info import GroupInfo
from src.theme.header import *
from src.theme.history_page import HistoryPage
from src.theme.home import Home
from src.theme.hot import Hot
from src.theme.navbar import *
from src.theme.search import SearchPage
from src.theme.sub_theme.detail_view import DetailView
from src.theme.sub_theme.list_view import *
from src.theme.sub_theme.login import Login
from src.theme.sub_theme.personal_info import PersonalInfo
from src.theme.sub_theme.pw_forget import PWForget
from src.theme.sub_theme.signup import Signup


class App:
    """_summary_
    """

    def __init__(self):
        Comic.load_comic_list()

        self.account_status = False
        self.user = None

        self.footer = Footer()
        self.header = Header(self)
        self.navbar = NavBar(self)

        self.home = Home(self)
        self.hot = Hot(self)
        self.following_page = FollowingPage(self)
        self.history_page = HistoryPage(self)
        self.app_download_page = AppDownload()
        self.group_info_page = GroupInfo()
        self.search_page = SearchPage(self)
        self.filter_page = FilterPage(self)
        self.detail_page = DetailView(self, 100000)

        self.login = Login(self)
        self.signup = Signup(self)
        self.pwforget = PWForget(self)

        self.personal_info = PersonalInfo(self)

        self.content = None

    def log_in(self):
        self.account_status = True
        # # Update user info hear ##############

        self.user = None

        self.header.content.content.content.controls[5] = self.header.account_header
        self.header.account_header.content.content.controls[0].value = "Dajunctic Vu"
        self.header.content.update()

    def sign_out(self, e: ft.ContainerTapEvent):
        self.account_status = False
        self.header.content.content.content.controls[5] = self.header.login_button

        # print(self.content.content.content.controls[5])
        self.header.content.content.content.update()

    def run(self, page: ft.Page):
        """_summary_

        Args:
            page (ft.Page): _description_
        """
        page.title = TITLE
        page.bgcolor = ft.colors.WHITE
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.scroll = "always"

        self.content = ft.Container(
            ft.Column(
                [
                    self.header.content,
                    self.navbar.content,

                    self.home.content,

                    self.footer.content,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0
            ),
            alignment=ft.alignment.center
        )

        page.add(self.content)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.run, assets_dir="assets")
    # ft.app(target=app.run, view=ft.WEB_BROWSER, assets_dir="assets")
