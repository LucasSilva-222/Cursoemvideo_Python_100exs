# Soma de todos os ímpares divisíviveis por 3
s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print('A soma de todos os valores impares divisíveis por 3 entre 1 e 500 é {}'.format(s))

