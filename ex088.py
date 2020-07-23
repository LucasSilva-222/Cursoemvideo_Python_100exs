from random import randint
from time import sleep
sortear = int(input('Quantos jogos quer sortear? '))
lista = list()
for c in range(0, sortear):
    print(f'Jogo {c+1}: ', end='')
    lista.clear()
    while len(lista) != 6:
        pc = randint(1, 60)     # gera um número aleatório e se ele não estiver na lista (not in) ele é adicionado a mesma
        if pc not in lista:
            lista.append(pc)
    print(lista)
    sleep(0.3)

