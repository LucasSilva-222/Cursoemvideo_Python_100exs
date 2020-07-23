# Repetição infinita com break
cont = 0
soma = 0
while True:
    n = float(input('Digite um valor [999] para parar: '))
    if n == 999:
        break
    soma += n  # fazer as contas depois de verificar se o número digitado é 999 para não incluilo.
    cont += 1
print(f'A soma dos {cont} valores digitados é igual a {soma}')
