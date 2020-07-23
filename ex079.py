# Valores unicos em uma lista
lista = list()  #lista vazia iniciada.
while True:     #inciada uma repetição infinita.
    num = int(input('Digite um valor:'))    # pede um número para o usuáro.
    if num not in lista:        # se o número não estiver na lista ele é adicionado pelo append.
        lista.append(num)
        print('Valor adicionado com sucesso!')
        print('-='*20)
    else:           # caso o contrário o número não e adicionado.
        print('O valor já se encontra na lista! Não foi adicionado')
        print('-=' * 20)
    while True:     # Outro while True para que n seja 's' ou 'n'
        n = str(input('Quer continuar [S/N]')).lower().strip()
        if n == 's' or n == 'n':    # caso n for s ou n ele vai sair do loop infinito
            break
    if n == 'n':    # se n for não ele irá sair do while True caso contrário ele voltará para o começo
        break
print(f'Você digitou os valores: {sorted(lista)}')   # Mostra os números adicionados em ordem crescente
