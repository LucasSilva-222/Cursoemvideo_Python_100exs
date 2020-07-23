lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista2 = 0
soma = 0
for c in range(0, 3):
    for ly in range(0, 3):
        lista[c][ly] = int(input(f'Digite um valor para a pocição [{c}, {ly}]'))
for l in range(0, 3):
    for cl in range(0, 3):
        print(f'[ {lista[l][cl]:^5} ]', end='')
    print()  # quebra a linha
for e in range(0, 3):
    soma += lista[e][2]     # Soma apenas ultimos valores da lista, pois eles ficam na 3 coluna
    for b in range(0, 3):
        if lista[e][b] % 2 == 0:    # se o número for par ele é somado a uma variável
            lista2 += lista[e][b]
print(f'A soma dos números pares digitados é: {lista2}')
print(f'O maior valor na 2 linha é: {max(lista[1])}')
print(f'A soma dos valores na 3 coluna é {soma}')
