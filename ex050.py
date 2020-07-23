# Somador de números pares
s = 0
x = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro [{} de 6]: '.format(c)))
    if n % 2 == 0:
        s += n
        x += 1
print('A soma dos {} valores pares digitados é igual A {}'.format(x, s))
