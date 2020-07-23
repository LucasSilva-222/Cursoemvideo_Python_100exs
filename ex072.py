# Números por extenso
ex = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    c = int(input('Digite um número de 0 à 10:'))
    while True:
        if 0 <= c <=10:
            break
        c = int(input('Tente novamente Digite um número de 0 à 10: '))
    print(f'{c} por extenso é: {ex[c]}')
    while True:
        continuar = str(input('Quer continuar?[S/N] ')).lower()
        if continuar == 's':
            break
        elif continuar == 'n':
            break
    if continuar == 'n':
        break
print('='*20)
print('{:^20}'.format('FIM'))
print('='*20)
