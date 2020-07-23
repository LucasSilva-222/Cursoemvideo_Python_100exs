# Pedra papel ou tesoura
from random import randint
from time import sleep
print('-=-'*20)
print('{:^60}'.format('Pedra, Papel ou Tesoura'))
print('-=-'*20)
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
js = float(input('Qual a sua jogada? '))
pc = randint(1, 3)
lista = ('pedra', 'papel', 'tesoura')
print('Pedra')
sleep(0.4)
print('Papel')
sleep(0.4)
print('Tesoura')
sleep(0.2)
if js == pc:
    print('\033[4;30mEmpate\033[m Computador escolheu {}'.format(lista[pc-1]))
elif js == 1 and pc == 2:
    print('\033[4;31mVocê Perdeu\033[m, Computador escolheu Papel!!!')
elif js == 1 and pc == 3:
    print('\033[4;34mVocê Ganhou!!!\033[m, Computador escolheu Tesoura!!!')
elif js == 2 and pc == 1:
    print('\033[4;34mVocê Ganhou!!!\033[m, Computador escolheu Pedra')
elif js == 2 and pc == 3:
    print('\033[4;31mVocê Perdeu\033[m, Computador escolheu Tesoura')
elif js == 3 and pc == 1:
    print('\033[4;31mVocê Perdeu\033[m, Computador escolheu Pedra')
elif js == 3 and pc == 2:
    print('\033[4;34mVocê Ganhou!!!\033[m, Computador escolheu Papel')
else:
    print('\033[4;36mOpção inválida!!!\033[m')
    



















