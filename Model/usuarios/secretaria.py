from Model.usuarios.usuario import User
class Secretaria(User):
    def __init__(self, id: str, nome: str, senha: str, nivel: str):
        super().__init__(id, nome, senha, nivel)


if __name__ == '__main__':

    secretaria1 = Secretaria("23", "pedro", "0637", "nivel2")


