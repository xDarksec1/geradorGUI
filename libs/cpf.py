from random import randint
import re


def valida(vcpf):
    vcpf = re.sub(r"[^0-9]", "", vcpf)
    cpf = vcpf
    newcpf = cpf[:-2]
    valor = 10
    soma = 0

    if len(cpf) != 11:
        return False

    for i in range(19):
        if i > 8:
            i -= 9
        soma += int(newcpf[i]) * valor
        valor -= 1
        if valor < 2:
            digito = 11 - (soma % 11)
            if digito > 9:
                digito = 0
            newcpf += str(digito)
            valor = 11
            soma = 0
    sequencial = cpf == newcpf[0] * len(cpf)

    if cpf == newcpf and not sequencial:
        return True
    else:
        return False


def gerarcpf(vezes=1):
    cont = 0
    lista = []
    while cont < vezes:
        newcpf = str(randint(000000000, 999999999))
        soma = 0
        valor = 10
        if len(newcpf) < 9:
            continue
        for i in range(19):
            if i > 8:
                i -= 9
            soma += int(newcpf[i]) * valor
            valor -= 1
            if valor < 2:
                digito = 11 - (soma % 11)
                if digito > 9:
                    digito = 0
                newcpf += str(digito)
                valor = 11
                soma = 0
        cont += 1
        sequencial = newcpf == newcpf[0] * len(newcpf)
        if not sequencial:
            lista.append(newcpf)
    return lista


if __name__ == "__main__":
    print(valida("10868026670"))
