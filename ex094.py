dici = dict()
lista = list()      # inicia uma lista e um dicionário
media = 0
while True:
    dici['Nome'] = str(input('Nome: ')).capitalize()        # No dicionário são colocadas as informações nome e idade
    dici['Idade'] = int(input('Idade: '))
    media += dici['Idade']      # as idades digidadas são somadas a variável media para serem subtridas em seguda
    while True:
        dici['Sexo'] = str(input('Sexo [M/F]')).lower()
        if dici['Sexo'] == 'm' or dici['Sexo'] == 'f':      # esquema da opção correta
            break
    lista.append(dici.copy())       # Faz uma copia do dicionário e o coloca em uma lista
    while True:
        choise = str(input('Quer continuar?[S/N]')).lower()     # Esquema do quer continuar
        if choise == 's' or choise == 'n':
            break
    if choise == 'n':
        break
print(f'Ao todo foram cadastras {len(lista)} pessoas')      # usa o len de lista para falar o tando de pessoas cadastradas
print(f'A media de idade do grupo é de {media/len(lista):.2f}')   # Divide o valor obtido com a soma das idades pelo tanto de pessoas cadastradas
print('As mulheres cadastradas foram: ', end='')
for y, x in enumerate(lista):
    if x['Sexo'] == 'f':        # x vira um dicionário em lista e se o sexo for igual a "f" o nome é printado
        print(x['Nome'], end=' ')
print()
print('As pessoas com idade acima da média registradas foram: ')
for a, b in enumerate(lista):       # O mesmo esquema é ultilzado para saber se a idade é acima da media
    if b['Idade'] > media/len(lista):
        print(f'{b["Nome"]} com {b["Idade"]}')
print()
