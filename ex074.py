# Gerador de números
from random import randint
while True:
    while True:
        n = str(input('Gerar números? [S / N]')).lower()
        if n == 's' or n == 'n':
            break
    if n == 'n':
        break
    c = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
    print(f'Números gerados: {c}\nMaior número: {max(c)}\nMenor número: {min(c)}')
