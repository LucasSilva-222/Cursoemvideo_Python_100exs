lista = [[], []]    #   Cria duas listas dentro de uma lista
for c in range(1, 8):
    n = int(input(f'Digite um valor para a posição {c}: '))
    if n % 2 == 0:      # se o valor for par ele é colocado na primeira lista lista [0]
        lista[0].append(n)
    else:       # se não ele é colocado na segunda lista[1]
        lista[1].append(n)
lista[0].sort()    # Organiza os valores em ordem crescente
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}\nOs valores ímpares digitados foram: {lista[1]} ')

