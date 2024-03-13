class Turma:
    def __init__(self, id:int, serie, identificador, anoLetivo, periodo):
        self.__id = id
        self.__serie = serie
        self.__indentficador = identificador
        self.__anoLetivo = anoLetivo
        self.__periodo = periodo


    @property
    def getId(self):
        return self.__id

    @property
    def getSerie(self):
        return self.__serie

    @property
    def getIdentificador(self):
        return self.__indentficador

    @property
    def getAnoLetivo(self):
        return self.__anoLetivo

    @property
    def getPeriodo(self):
        return self.__periodo