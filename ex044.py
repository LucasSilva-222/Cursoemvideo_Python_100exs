print('{:=^40}'.format('Lucas Lojas'))
p = float(input('Qual o valor do produto? '))
print('Escolha a opção de pagamento')
print('[ 1 ] À vista dinheiro/Cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Em até 2X no cartão')
print('[ 4 ] 3X ou mais no cartão')
n = int(input('Escolha uma opção: '))
op = [p*0.10, p*0.05, p, p*0.20]
if n == 1:
    print('O produto pago à vista em dinheiro ou cheque ira custar \033[32m{}R$\033[m'.format(p - op[0]))
elif n == 2:
    print('O produto pago à vista no cartão irá custar \033[32m{}R$\033[m'.format(p - op[1]))
elif n == 3:
    print('O produto parcelado em 2 vezes irá custar \033[32m{:.2f}R$\033[32m em 2X de \033[4;32m{}R$\033[m sem juros!!'.format(p, p/2))
elif n == 4:
    n2 = int(input('Quantas parcelas? '))
    print('O produto de {}r$ parcelado em {}X ira custar {} com parcelas de {:.2f} por mes'.format(p, n2, p +op[3], (p+op[3])/n2))

else:
    print('\033[4;31mOpçao inválida!, tente novamente')














