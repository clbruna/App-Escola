from Model.usuarios.professor import Professor
from faker import Faker
import random


def geradorSenhas():
    n1= str(random.randint(0,9))
    n2 = str(random.randint(0, 9))
    n3 = str(random.randint(0, 9))
    n4 = str(random.randint(0, 9))
    return f"{n1}{n2}{n3}{n4}"


names=Faker()

constanteNiveis=["COMUM","ADM", "GERENTE"]
constanteContrato=["CLT","ESTAGIO", "EVENTUAL"]
print(names.name())

for i in range(100):
    id = random.randint(0, 9)
    senha = geradorSenhas()

    cons_Niv=[e for e in constanteNiveis]
    p1=Professor(str(id),names.name(),senha,"COMUM", "CLT")

    print(f"teste ID: {p1.getId.isdecimal()}")
    print(f"teste nome:  {isinstance(p1.getNome,str)}")
    print(f"teste senha: {p1.getSenha.isdecimal()}")
    print(f"teste nivel: {p1.getNivel.isalpha()}")
    print(f"teste contrato: {p1.contrato.isalpha()}")
    print("#"*40)


