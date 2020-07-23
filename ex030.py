# Par ou Ímpar?
print('{:=^40}'.format('Par ou ímpar?'))
n = float(input('Digite um número: '))
if n % 2 == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar'.format(n))



