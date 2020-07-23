# Maior peso
maior = 0
menor = 0
for c in range(1, 6):
    n = float(input('Digite um peso [{} de 5]: '.format(c)))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))

