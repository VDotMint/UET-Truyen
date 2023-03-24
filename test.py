from settings import *
from src.theme.footer import *
from src.theme.header import *
from src.theme.navbar import *
from src.theme.sub_theme.login import *
from src.theme.sub_theme.signup import *
from src.theme.sub_theme.recommendation import *

class App:
    def __init__(self):
        self.footer = Footer()
        self.header = Header()
        self.navbar = NavBar()
        self.login = Login()
        self.signup = Signup()
        self.recommendation = Recommendation()

    def run(self, page: ft.Page):
        page.title = TITLE
        page.bgcolor = ft.colors.WHITE
        page.scroll = "always"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        page.add(self.recommendation.content)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.run, assets_dir="assets")
    # ft.app(target=app.run, view=ft.WEB_BROWSER, assets_dir="assets")
