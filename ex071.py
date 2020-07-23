print('{:=^20}'.format('='))
print('{:^20}'.format('Lucas Bancos'))
print('{:=^20}'.format('='))
print('Notas disponíveis: 50R$ 20R$ 10R$ 1R$')
n = int(input('Quanto vai sacar?'))
c50 = 0
c20 = 0
c10 = 0
c1 = 0
while True:
    if n // 50 != 0:
        c50 = n // 50
        n = n % 50
    elif n // 20 != 0:
        c20 = n // 20
        n = n % 20
    elif n // 10 != 0:
        c10 = n // 10
        n = n % 10
    else:
        c1 = n // 1
        n = n % 1
    if n == 0:
        break
print(f'{c50} cedulas de 50R$\n{c20} cedulas de 20R$\n{c10} cedulas de 10R$\n{c1} cedulas 1 R$')


