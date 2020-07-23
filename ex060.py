# Fatorial !
n = int(input('Digite um número:'))
c = n
f = 1
print('Calculando......')
while c > 0:
    print('{} '.format(c), end='')
    print('= ' if c == 1 else 'x ', end='')
    f = f *c
    c -= 1
print(f)

