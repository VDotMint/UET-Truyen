"""_summary_
    """
import flet as ft
from settings import TITLE


class App:
    """_summary_
    """

    def __init__(self):
        #
        pass

    def run(self, page: ft.Page):
        """_summary_

        Args:
            page (ft.Page): _description_
        """
        page.title = TITLE
        page.bgcolor = ft.colors.WHITE
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        content = ft.Row(
            [
                ft.Image(src="assets/icons/loading-animation.png"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        page.add(content)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.run, assets_dir="assets")
    # ft.app(target=app.run, view=ft.WEB_BROWSER, assets_dir="assets")
