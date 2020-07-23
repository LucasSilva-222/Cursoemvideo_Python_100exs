from time import sleep
def p1():           # Função para dar print =
    print('='*30)
def contador(i, f, p):
    if p == 0:      # Se o passo for 0 para não dar erro 1 é contabilizado
        p += 1
    if p > 0:
        print(f'Contagem de {i} até {f} de {p} em {p}')         # contagem que vai do inicio (i) até o final (f) pulando de (p) em (p)
    elif p < 0:
        print(f'Contagem de {i} até {f} de {p*-1} em {p*-1}')
        p = p*-1
    if i <= f:      # se o número for maior ou igual ao final o saldo não sera negativo
        for c in range(i, f+1, p):      # Um for é feito para a contagem f+1 pois o for ignora o ultimo valor
            print(c, end=' ')
            sleep(0.3)
        print()
        p1()
    else:
        for a in range(i, f-1, -p):
            print(a, end=' ')
            sleep(0.3)
        print()
        p1()
contador(1, 10, 0)
contador(10, 0, 2)
p1()
start = int(input('Qual o começo? '))
ende = int(input('Qual o final? '))
passo = int(input('Qual é o passo? '))
contador(start, ende, passo)




