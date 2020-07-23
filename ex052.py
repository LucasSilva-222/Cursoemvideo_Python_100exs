# Número primo?
v = 0
n = int(input('Digite um número inteiro:'))
for c in range(1, n+1):
    if n % c == 0:
        v += 1
if v == 2:
    print('É um número primo')
else:
    print('Não é um número primo')
