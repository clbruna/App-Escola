class User:
    def __init__(self, id: str, nome: str, senha: str, nivel: str):

        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__nivel = nivel


    @property
    def getId(self):
        return self.__id

    @property
    def getNome(self):
        return self.__nome

    @property
    def getSenha(self):
        return self.__senha

    @property
    def getNivel(self):
        return self.__nivel


    @getNome.setter
    def setNome(self, nome):
        self.__nome = nome

    @getSenha.setter
    def setSenha(self, senha):
        self.__senha = senha

