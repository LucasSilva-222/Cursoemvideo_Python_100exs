# Alugel de carro custa 60 reais por dia e 0.15 centavos por km rodado
print('{:=^40}'.format('Contador de aluguel'))
dias = float(input('Quantos dias você ficou com o carro? '))
kmr = float(input('Quantos Km você rodou? '))
precofinal = (dias*60) + (kmr*0.15)
print('Valor total a pagar {}R$'.format(precofinal))


