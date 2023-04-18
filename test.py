from settings import *
from src.theme.footer import *
from src.theme.header import *
from src.theme.navbar import *
from src.theme.sub_theme.chapter_view import Chapter
from src.theme.sub_theme.login import *
from src.theme.sub_theme.signup import *
from src.theme.sub_theme.recommendation import *
from src.theme.sub_theme.following import *
from src.theme.sub_theme.top import *
from src.theme.sub_theme.detail_view import *
from src.theme.sub_theme.list_view import *

class App:
    def __init__(self):
        self.footer = Footer()
        self.header = Header()
        self.navbar = NavBar()
        # self.chapter = Chapter()
        self.login = Login()
        self.signup = Signup()
        self.recommendation = Recommendation(app)
        self.following = Following()
        self.top = Top()
        self.detail_view = DetailView()
        self.latest = ListView()

    def run(self, page: ft.Page):
        page.title = TITLE
        page.bgcolor = ft.colors.BLACK
        page.scroll = "always"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        page.add(self.detail_view.content)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.run, assets_dir="assets")
    # ft.app(target=app.run, view=ft.WEB_BROWSER, assets_dir="assets")
