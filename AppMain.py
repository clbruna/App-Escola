from flet import *

from Views.viewLogin import ViewLogin


def main(page:Page):

    telaLogin = ViewLogin()

    def changeRoutes(route):

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[telaLogin]
            )
        )

        page.update()




    page.on_route_change = changeRoutes
    page.go(page.route)





if __name__ == '__main__':
    app(target=main, assets_dir="assets")