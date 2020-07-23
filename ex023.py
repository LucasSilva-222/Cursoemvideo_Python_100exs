# Unidade dezena centena e milhar
num = str(input('Digite um número inteiro de 0 a 9999: '))
num2 = num.strip()
print('Unidade: {}'.format(num2[3]))
print('Dezena: {}'.format(num2[2]))
print('Centena: {}'.format(num2[1]))
print('Milhar: {}'.format(num2[0]))


