from Model.usuarios.secretaria import Secretaria
class Administradores(Secretaria):
    def __init__(self,id: str, nome: str, senha: str, nivel: str):
        super().__init__(id, nome, senha, nivel)