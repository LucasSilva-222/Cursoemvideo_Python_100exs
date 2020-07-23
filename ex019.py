# sorteio de alunos
from random import choice

a1 = input('Digite o 1 nome: ')
a2 = input('Digite o 2 nome: ')
a3 = input('Digite o 3 nome: ')
a4 = input('Digite o 4 nome: ')
escolha = (a1, a2, a3, a4)
print('O aluno sorteado foi {}'.format(choice(escolha)))

