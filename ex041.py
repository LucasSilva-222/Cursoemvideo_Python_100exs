from datetime import date
a = date.today().year
b = float(input('Digite seu ano de nascimento para saber sua categoria: '))
i = a - b
print('O atleta tem {} anos'.format(i))
print('Categoria:')
if b > a:
    print('Data inválida')
elif i <=9:
    print('Mirim')
elif 9 < i < 15:
    print('Infantil')
elif 15 < i < 20:
    print('Júnior')
elif i == 20:
    print('Sênior')
else:
    print('Master')





