import os
from random import sample


def sortear():
    listas = list(range(1, 31)) * 15
    sorteado = sample(lista, 1)[0]
    if sorteado not in sorteados:
        sorteados.append(sorteado)
        os.system("clear")
        for i in listas + [sorteado]:
            os.system("clear")
            print(i, "PARABÉNS!")
    else:
        sortear()


start = int(input("Inicial: "))
end = int(input("Final: "))

lista = range(start, end + 1)

try:
    sorteados = []
    while True:
        if sorteados:
            print("\nSorteados: ", sorteados)
        enter = input("\nENTER ")
        if enter == "":
            sortear()
        else:
            break

except RecursionError:
    print("Bye!")
