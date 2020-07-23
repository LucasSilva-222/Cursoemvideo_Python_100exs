# Tabuada com flag e break
while True:
    n = int(input('Qual valor deseja ver? '))
    if n <= 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n} X {c} = {n*c}')
            c += 1
print('Programa finalizado com sucesso! volte sempre!')


