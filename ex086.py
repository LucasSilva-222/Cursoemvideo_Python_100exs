lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for ly in range(0, 3):
        lista[c][ly] = int(input(f'Digite um valor para a pocição [{c}, {ly}]'))
for l in range(0, 3):
    for cl in range(0, 3):
        print(f'[ {lista[l][cl]} ]', end='')
    print()     #quebra a linha



