# Tipo de triângulo
r = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de mais uma reta: '))
r3 = float(input('Digite o comprimento da ultima reta: '))
if r + r2 > r3 and r + r3 > r2 and r2 + r3 > r:
    print('As retas PODEM formar um triângulo', end='')
    if r == r2 == r3:
        print(' EQUILÁTERO')
    elif r != r2 != r3 != r:
        print(' ESCALENO')
    else:
        print(' ISÓCELES')
else:
    print('As retas NÃO PODEM formar um triângulo')






