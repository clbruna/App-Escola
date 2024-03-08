class Materia:
    def __init__(self, id: str, nome: str):
        self.__id = id
        self.__nome = nome


    @property
    def getMateria(self):
        return self.__nome

    @property
    def getId(self):
        return self.__id