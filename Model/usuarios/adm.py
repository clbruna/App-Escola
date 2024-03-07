from usuario import User
class Adm(User):
    def __init__(self, id: str, nome: str, senha: str, nivel: str):
        super().__init__(id, nome, senha, nivel)