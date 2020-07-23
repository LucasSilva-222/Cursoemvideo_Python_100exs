# Funções para somar e gerar numeros aleatórios
from random import randint
from time import sleep
def sortear(lst):
    for c in range(1, 6):
        lst.append(randint(1, 10))
    print(f'Sorteando... ', end='')
    for c in lst:
        print(c, end=' ')
        sleep(0.3)
    print()
def somapar(lst2):
    sump = 0
    print(f'Somando todos os valores pares de {lst2}')
    for c in lst2:
        if c % 2 == 0:
            sump += c
    print(f'A soma é igual à {sump}')
lista = []
sortear(lista)
somapar(lista)

