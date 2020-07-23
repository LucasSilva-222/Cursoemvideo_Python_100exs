# lista aleatoria de alunos
from random import shuffle
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')
lista = [a1, a2, a3, a4]
shuffle(lista)  # shuffle embaralha os itens presentes na lista
print(f'A ordem sorteada foi {lista}')

