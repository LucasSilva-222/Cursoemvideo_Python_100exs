# se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo
r = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de mais uma reta: '))
r3 = float(input('Digite o comprimento da ultima reta: '))
if r + r2 > r3 and r + r3 > r2 and r2 + r3 > r:
    print('As retas PODEM formar um triângulo')
else:
    print('As retas NÃO PODEM formar um triângulo')




