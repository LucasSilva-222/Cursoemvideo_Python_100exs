# Imc
a = float(input('Quantos você tem de altura? '))
p = float(input('Quantos você pesa? '))
imc = p/(a * a)
imc2 = imc
print('Uma pessoa que pesa {}Kg e mede {}m tem o imc de {:.2f} isso indica:'.format(p, a, imc))
if imc >=0 and imc2 <=18.5:
    print('Peso abaixo do ideal!')
elif imc >18.5 and imc2 <=25:
    print('Peso ideal!')
elif imc >25 and imc2 <=30:
    print('Sobre peso!')
elif imc >30 and imc2 <=40:
    print('Obesidade!')
else:
    print('Obesidade Morbida!')



