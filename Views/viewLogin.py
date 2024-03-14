from flet import *

class ViewLogin(UserControl):


    def __init__(self):
        super().__init__()
        self.logo = Image(src=r"logotipo.png")
        self.titleView = Text("FAÇA LOGIN")
        self.t_field_Login = TextField(label="Usuario")
        self.t_field_Password = TextField(label="Senha")
        self.btn_Enter = ElevatedButton("ENTRAR")



    def build(self):

        layout = ResponsiveRow(
            controls=[
                Column(controls=[self.logo]),
                Row(controls=[self.titleView]),
                Column(controls=[self.t_field_Login]),
                Column(controls=[self.t_field_Password]),
                Column(controls=[self.btn_Enter])
            ]
        )


        return layout
