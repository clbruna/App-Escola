from Model.usuarios.professor import Professor
from faker import Faker
import random
import re

def geradorSenhas():
    n1= str(random.randint(0,9))
    n2 = str(random.randint(0, 9))
    n3 = str(random.randint(0, 9))
    n4 = str(random.randint(0, 9))
    n5 = str(random.randint(0, 9))
    return f"{n1}{n2}{n3}{n4}{n5}"


names=Faker()

constanteNiveis=["COMUM","ADM", "GERENTE"]
constanteContrato=["CLT","ESTAGIO", "EVENTUAL"]

def testarNivel(nivel):

    if nivel in constanteNiveis:
        return True
    else:
        return False

def testaNome(nome:str) ->bool:
    """
    realiza um teste no campo nome
    >> nome== "José"

    :param nome:
    :return: bool
    """
    regex_nome = r'^[a-zA-ZÀ-ÿ\'\s]+$'
    if re.match(regex_nome, nome):
        return True
    else:
        return False


def testarSenha(senha:str)-> bool:

    regex_senha= r'^.*\d{4}.*$'
    if re.match(regex_senha,senha):
        return True
    else:
        return False

def testarContrato(contrato:str)->bool:
    if contrato in constanteContrato:
        return True
    else:
        return False


for i in range(100):
    id = random.randint(0, 100)
    senha = geradorSenhas()
    contrato= random.choice(constanteContrato)
    niveis=random.choice(constanteNiveis)

    cons_Niv=[e for e in constanteNiveis]
    p1=Professor(str(id),names.name(),senha,niveis, contrato)
    print(f"Teste {i}")
    print(f"teste ID: {p1.getId.isdecimal()}, id testado {id}")
    print(f"teste nome:  {testaNome(p1.getNome)}, nome testado {p1.getNome} ")
    print(f"teste senha: {testarSenha(p1.getSenha)}, senha testado {p1.getSenha}   ")
    print(f"teste nivel: {testarNivel(p1.getNivel)},  nivel testado {p1.getNivel}")
    print(f"teste contrato: {testarContrato(p1.contrato)}, nivel contrato {p1.contrato}  ")
    print("#"*40)


