# Maior menor com while
t = ''  # string vazia pois while não aceita declaraçao de variaveis de controle
maior = 0
menor = 0
c = 0
soma = 0
while t != 'n':
    n = int(input('Digite um valor: '))
    t = str(input('Quer continuar [S/N]? ')).lower().strip()
    while 'n' != t != 's':
        if t != 's':
            print('Resposta inválida digite [S ou N]')
            t = str(input('Quer continuar [S/N]? ')).lower().strip()
    if c == 0:
        maior = n
        menor = n
    if c > 1 and n >maior:
        maior = n
    if c > 1 and n < menor:
        menor = n
    c += 1
    soma += n
print('A media entre os valores é de: {:.2f}'.format(soma/c))
print('O maior valor detectado foi {} e o menor {}'.format(maior, menor))

