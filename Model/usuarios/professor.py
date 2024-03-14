from Model.materia import Materia
from Model.usuarios.usuario import User
from Model.aula import Aula

class Professor(User):
    def __init__(self, id:int, nome: str, senha: str, nivel: str, contrato: str):
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


    #metodos
    def addMateria(self, materia:Materia):
        if type(materia) == Materia:
            self.__materias.append(materia)
        else:
            print("vode pode adicionar materias")

    def addAula(self, aula:Aula):
        if type(aula) != Aula:
            print("nao foi possivel adicionar")
        else:
            self.__aulas.append(aula)
            print("Aula cadastrada com sucesso!")

    def verMaterias(self):
        for materia in self.__materias:
            print(f"ID:{materia.id} | Nome:{materia.nome}")

    def verAulas(self):
        for aula in self.__aulas:
            print(f"ID:{aula.idAula} | Turma:{aula.idTurma.serie}{aula.idTurma.identificador} | aula:{aula.numeroAula} | Data:{aula.data}")
