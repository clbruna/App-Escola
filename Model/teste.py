from usuarios.professor import Professor
from usuarios.gerencia import Administradores
from usuarios.secretaria import Secretaria
from materia import Materia
from aula import Aula
from turama import Turma

#============================= Usuarios ================================

prof1 = Professor("1", "Carlos", "12345", "comum", "clt")

prof2 = Professor("3", "Jose", "12345", "comum", "clt")

prof3 = Professor("6", "Maria", "12345", "comum", "clt")

prof4 = Professor("11", "Ana", "12345", "comum", "clt")

secretaria1 = Secretaria("23", "pedro", "0637", "nivel2")

secretaria2 = Secretaria("2","Leticia", "11745", "nivel3")

gerencia1 = Administradores("99","Agata", "12345", "nivel3")

#================================ Materias ===============================

materia1 = Materia("1", "Matematica")
materia2 = Materia("4", "Português")
materia3 = Materia("5", "Historia")
materia4 = Materia("7", "Fisíca")
materia5 = Materia("12", "Geografia")

#============================= Turmas =====================================

turma1 = Turma("3", "2", "A", "2023","manha")

turma2 = Turma("4", "5", "F", "2023","manha")

turma3 = Turma("5", "7", "B", "2023","manha")

turma4 = Turma("6", "2", "D", "2023","manha")

#============================= Aulas ======================================

Aula1 = Aula(turma1.getSerie, turma1.getIdentificador, prof1.getNome, materia1.getMateria, "1", "20/03/2024")

materia1.addProfessor(prof2.getNome)
materia1.addProfessor(prof3.getNome)




