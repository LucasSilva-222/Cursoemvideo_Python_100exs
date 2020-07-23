# Par ou Impar
from random import randint
perdeu = 0
ganhou = 0
while True:
    pc = randint(1, 11)
    print('{:=^20}'.format('='))
    print('Par ou Ímpar!')
    print('{:=^20}'.format('='))
    n = int(input('Digite um número:'))
    while True:
        pi = str(input('Par ou Impar?[P/I] ')).lower()
        if 'i' == pi or 'p' == pi:
            break
    total = pc + n
    print(f'O computador escolheu {pc} e você {n} dando um total de {total}')
    if total % 2 == 0:
        if pi == 'p':
            print('PAR!!! VOCÊ GANHOU!')
            ganhou +=1
        else:
            print('Deu par.... VOCÊ PERDEU!')
            perdeu +=1
    else:
        if pi == 'i':
            print('ÍMPAR!!! VOCÊ GANHOU ')
            ganhou +=1
        else:
            print('Deu ímpar... VOCÊ PERDEU')
            perdeu += 1
    if perdeu == 1:
        break
print(f'Você ganhou um total de {ganhou} vezes!!')
