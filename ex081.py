lista = list()  # Cria uma lista
value = 0       # inicia uma variável com o intuito de contagem
while True:      # while True para ler os números indefinidamente
    n = int(input('Digite um número: '))        # pergunta um número
    lista.append(n)     # Adiciona o número na lista
    while True:     # Outro while True para a pergunta sobre continuidade ou não do programa
        value +=1   # value para ver quantos números foram digitados
        s = str(input('Quer continuar?[S/N] '))
        if s == 'n' or s == 's':        # condição de saida
            break
    if s == 'n':    # condição de termino
        break
print(f'Você digitou {value} elementos')
lista.sort(reverse=True)
print(f'Em ordem decrescente os números foram {lista}')
print('O valor 5 faz parte da lista' if 5 in lista else 'O valor 5 não foi detectado')

