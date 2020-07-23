listag = list()
v = 0
while True:
    temp = [str(input('Nome aluno:')).capitalize(), float(input('Nota 1 do aluno: ')), float(input('Nota 2 do aluno: '))]
    listag.append(temp)
    while True:
        choise = str(input('Quer continuar? [S/N] ')).lower()
        if choise == 'n' or choise == 's':
            break
    if choise == 'n':
        break
print('-='*30)
print('No.    NOME              MÉDIA')
print('-'*30)
for x in range(0, len(listag)):         # x vai de 0 até o len de lista(como o ultimo valor é iguinorado no for não precisamos colocar -1 para não dar erro nos indicies
    print(f'\n{x:<5}  {listag[x][0]:<15} {(listag[x][1]+listag[x][2])/2:^8} ')              # primeiro queremos ver a posisão, depois o nome nessa posição, e por fim a média das notas que estão no final.
print('-'*30)
while v != 999:
    v = int(input('Quer mostrar qual aluno? [999] para parar (No.)'))
    if v > len(listag)-1 or v < 0:  # aqui é fita uma verificação se o valor digitado esta dentro de len, -1 pois a contagem de len começa de 1 e o indicie sempre vai ate -1 de len
        print('Aluno não cadastrado!')
        print('-='*20)
    else:   # caso o valor de v for um indicie possível e sem erro em listag as informações da sublista pedida são mostradas
        print(f'As notas de {listag[v][0]} são {listag[v][1]} e {listag[v][2]}')
        print('-='*20)










