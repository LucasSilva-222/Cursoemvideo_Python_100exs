# Ano Bissexto
print('{:=^40}'.format('Ano Bissexto'))
ano = float(input('Em que ano você esta?'))
if ano % 4 == 0:
    print('{} é um ano bissexto'.format(ano))
elif int(ano) % 4 != 0:
    print('{} não é um ano bissexto'.format(ano))







