from random import randint
import re


def checkcnp(cnpj):
    soma = 0
    valor = 5
    cnpj = re.sub(r"[^0-9]", "", cnpj)

    if len(cnpj) > 12:
        newcnpj = cnpj[:-2]
    else:
        newcnpj = cnpj

    if len(newcnpj) != 12 or newcnpj == "":
        return print(f"Impossível verificar o cnpj: {cnpj} ")

    for i in range(25):
        if i > 11:
            i -= 12
        soma += int(newcnpj[i]) * valor
        valor -= 1
        if valor < 2:
            valor = 9
        if (i == 11 and len(newcnpj) == 12) or (i == 12):
            digito = 11 - (soma % 11)
            if digito > 9:
                digito = 0
            soma = 0
            valor = 6
            newcnpj += str(digito)

    if newcnpj == newcnpj[0] * len(newcnpj):
        print("É uma sequência...INVÁLIDO!!")
    elif newcnpj == cnpj:
        print("\033[32mCNPJ VÁLIDO\033[m")
    else:
        print("\033[31mCNPJ INVÁLIDO\033[m")


def geracnp(qtde):
    cont = 0
    while cont < qtde:
        newcnpj = str(randint(00000000, 99999999)) + "0001"
        if len(newcnpj) < 12:
            continue
        valor = 5
        soma = 0
        for i in range(25):
            if i > 11:
                i -= 12
            soma += int(newcnpj[i]) * valor
            valor -= 1
            if valor < 2:
                valor = 9
            if (i == 11 and len(newcnpj) == 12) or (i == 12):
                digito = 11 - (soma % 11)
                if digito > 9:
                    digito = 0
                soma = 0
                valor = 6
                newcnpj += str(digito)
        print(formatacnpj(newcnpj), end=" -> ")
        checkcnp(newcnpj)
        cont += 1


# 01 234 567 8912 34
# 04.252.011/0001-10
def formatacnpj(num):
    return f"{num[:2]}.{num[2:5]}.{num[5:8]}/{num[8:12]}-{num[12:]}"
