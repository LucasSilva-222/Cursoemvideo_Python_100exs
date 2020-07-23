# Advinhação V2
from random import randint
print('='* 50)
print('{:^40}'.format('Vou pensar em um número de 0 a 10 tente adivinhar!'))
print('='* 50)
n = 0
pc = randint(1, 10)
c = 0
while n != pc:
    n = int(input('Sua escolha: '))
    if n < pc:
        print('Mais...', end='')
    if n > pc:
        print('Menos...)', end='')
    if n != pc:
        print(' Quase lá você consegue!')
        c += 1
print('Parabens você consegiu com {} tentativas!!'.format(c+1))
print('O numero que eu pensei era {}'.format(pc))
