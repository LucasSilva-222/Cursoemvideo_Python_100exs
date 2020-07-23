# Maior e menor valores na lista
lista = list()  # iniciei uma lista vazia
for c in range(1, 5):   # criei um for que irá repitir 4 vezes
    dig = int(input(f'Digite um número para a posição {c}: '))  # Um imput para o usuario colocar um valor
    lista.append(dig)   # adiciona os valores a lista
print(f'Os valores adicionadas foram: {lista}')  # Mostra os valores da lista ao final do for
print(f'O maior valor foi {max(lista)} e foi encontrado nas posições: ', end='')   # Mostra o maior valor
for x, y in enumerate(lista):   # cria um contador que recebe a pocição de lista (x) e um contador que recebe o valor dessa pocição(y)
    if y == max(lista):  # se y for igual ao valor máximo contido em lista
        print(f'{x+1} ', end='')    # ele vai mostrar a pocição (x) em que encontrou esse número, +1 pois a contagem em python inicia do 0
print(f'\nO menor valor foi {min(lista)} e foi encontrado nas posições: ', end='')    # mesma coisa só que com o menor valor ;)
for n, an in enumerate(lista):
    if an == min(lista):
        print(f'{n+1} ', end='')

