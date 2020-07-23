# Cobrador de multas
print('{:=^40}'.format('Radar Eletronico?'))
n = int(input('Digite sua velocidade: '))
limite = n - 90
multa = limite * 7
if n > 90:
    print('Multado Valor total a pagar {}R$'.format(multa))
else:
    print('Dentro do limite, use sempre o cinto de segurança')
print('Velocidade detectada: {}Km/h '.format(n))



