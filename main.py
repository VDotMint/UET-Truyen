from settings import *


class App:
    def __init__(self):
        pass

    def run(self, page: ft.Page):
        page.title = TITLE
        page.bgcolor = ft.colors.WHITE
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        content = ft.Row(
            [
                ft.image.Image(src="assets/icons/loading-animation.png"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        page.add(content)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.run, assets_dir="assets")
    # ft.app(target=app.run, view=ft.WEB_BROWSER, assets_dir="assets")
