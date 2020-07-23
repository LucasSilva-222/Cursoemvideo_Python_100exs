lg = []     # incia a lista geral a de pares e a de impares
lp = []
li = []
while True:
    n = int(input('Digite um valor: '))
    lg.append(n)
    while True:
        con = str(input('Quer continuar? [S/N]')).lower()
        if con == 's' or con == 'n':
            break
    if con == 'n':
        break
for c in lg:
    if c % 2 == 0:      # verifica se é par e adiciona na lista par
        lp.append(c)
    else:   # se não for adiciona na lista ímpar
        li.append(c)
print('-='*20)
print(f'A lista completa é {lg}\nOs valores pares são {lp}\nOs valores ímpares são {li}')


