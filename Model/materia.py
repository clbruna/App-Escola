class Materia:
    def __init__(self, id: int, nome: str):
        self.__id = id
        self.__nome = nome
        self.__professores = []


    @property
    def getMateria(self):
        return self.__nome

    @property
    def getId(self):
        return self.__id

    @property
    def professores(self):
        return self.__professores

    def addProfessor(self, professor):
        self.__professores.append(professor)

#apenas um teste
