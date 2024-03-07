from usuario import User
class Professor(User):
    def __init__(self, id: str, nome: str, senha: str, nivel: str):
        super().__init__(id, nome, senha, nivel)

