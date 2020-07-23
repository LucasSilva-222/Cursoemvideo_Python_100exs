# Lista composta
lista, dados, maior = [], [], []                     # 3 listas as duas primeiras com o intuido de criar uma lista composta e a ultima armazenar números
while True:
    p = ''
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])  # faz uma copia por conta do [:]
    dados.clear()
    while p != 's' and p != 'n':            # Famoso esquema do quer continuar já expliquei mil vezes
        p = str(input('Quer continuar? [S/N]')).lower()
    if p == 'n':
        break
print(f'Ao todo, foram cadastradas {len(lista)} pessoas')   # o len de listas (comprimento é o tanto de pessoas registradas)
for c in lista:         # armazenar todos os que forem números na lista maior[] como c se torna um dos itens e cada item, nesse caso, é composto por 2 valores [0] é o nome e [1] é o peso
    maior.append(c[1])
print(f'O maior peso encontrado foi {max(maior)}Kg e pertence a: ', end='')     # fala o maior número
for b in lista:
    if b[1] == max(maior):      # se o número verificado for o maior
        print(f'[{b[0]}]', end='')
print(f'\nO menor peso encontrado foi  {min(maior)}Kg e pertence a: ', end='')
for w in lista:     # faz a mesma coisa só que com o menor, só troquei as letras de todos os for pois n sei se da interferencia provalvelmente da.
    if w[1] == min(maior):
        print(f'[{w[0]}] ')

