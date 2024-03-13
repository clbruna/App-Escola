from Model.usuarios.usuario import User

class Professor(User):
    def __init__(self, id: str, nome: str, senha: str, nivel: str, contrato: str):
        super().__init__(id, nome, senha, nivel)
        self.__contrato = contrato
        self.__materias = []
        self.__aulas = []


    @property
    def contrato(self):
        return self.__contrato

    @property
    def materias(self):
        return self.__materias


    @materias.setter
    def materias(self, materia):
        self.__materias.append(materia)

    @property
    def aulas(self):
        return self.__aulas

    @aulas.setter
    def aulas(self, aula):
        self.__aulas.append(aula)



