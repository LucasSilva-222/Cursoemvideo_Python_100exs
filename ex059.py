# menu
from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro: '))
op = 0
while op != 5:
    op = int(input('''O que deseja fazer?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Número
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    Sua opção: '''))
    if op == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('A multiplicação {} e {} resultam em {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 == n2:
            print('Os dois valores digitados são iguais!')
        elif n1 > n2:
            print('{} é o maior valor inserido'.format(n1))
        else:
            print('{} foi o maior valor inserido'.format(n2))
    elif op == 4:
        n1 = float(input('Digite o novo valor: '))
        n2 = float(input('Digite outro valor: '))
    elif op == 5:
        print('Saindo')
    else:
        print('\033[4;31mOpçao Inválida\033[m')
    sleep(1)
print('Processo finalizado tenha um bom dia!')

