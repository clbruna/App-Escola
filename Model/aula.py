class Aula:
    def __init__(self, idAula, ident_Turma, idProfessor, idMateia, numeroAula, data, status=False):

        self.__idAula = idAula
        self.__identTurma = ident_Turma
        self.__idProfessor = idProfessor
        self.__idMateia = idMateia
        self.__numeroAula = numeroAula
        self.__data = data
        self.__status = status


    @property
    def idAula(self):
        return self.__idAula

    @property
    def idTurma(self):
        return self.__identTurma

    @property
    def idProfessor(self):
        return self.__idProfessor

    @property
    def idMateria(self):
        return self.__idMateia

    @property
    def numeroAula(self):
        return self.__numeroAula

    @property
    def data(self):
        return self.__data

    @property
    def status(self):
        return self.__status

    @idTurma.setter
    def setIdturma(self,idTurma):
        self.idTurma = idTurma

    @idProfessor.setter
    def setIdProfessor(self,idProfessor):
        self.__idProfessor = idProfessor

    @idMateria.setter
    def setIdMateria(self, idMateria):
        self.__idMateia = idMateria

    @numeroAula.setter
    def setNumeroAula(self, numeroAula):
        self.__numeroAula = numeroAula

    @data.setter
    def setData(self, data):
        self.__data = data

    @status.setter
    def setStatus(self, status):
        self.__status = status









