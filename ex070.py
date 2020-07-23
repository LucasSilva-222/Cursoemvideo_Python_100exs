# Carrinho Supermercado
dc = 0
bu = 0
gt = 0
menor = ''
cont = 1
menorval = 0
while True:
    g = int(input('Informe valor do produto: '))
    n = str(input('Informe o nome do produto: '))
    gt += g
    if cont == 1:
        menor = n
        menorval = g
    elif g < menorval:
        menor = n
        menorval = g
    if g > 1000:
        bu += 1
    while True:
        dc = input('Deseja continuar?[S/N] ').lower()
        if dc == 's':
            break
        elif dc == 'n':
            dc = 1
            break
    cont += 1
    if dc == 1:
        break
print(f'O total de gastos foi de {gt}R$\nAo todo {bu} produtos custam mais se 1000R$\nO mais barato se chama {menor} e custou {menorval}R$')


