from flet import *

from Views.viewLogin import ViewLogin
from Views.viewHome import ViewHome


def main(page:Page):

    telaLogin = ViewLogin()
    barHome = ViewHome()
    telaLogin.btn_Enter.on_click = lambda e: page.go("/home")

    def changeRoutes(route):

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[telaLogin]
            )
        )

        if page.route == "/home":
            page.views.append(
                View(
                    route="/home",
                    controls=[
                        barHome
                    ]
                )
            )

        page.update()




    page.on_route_change = changeRoutes
    page.go(page.route)





if __name__ == '__main__':
    app(target=main, assets_dir="assets")