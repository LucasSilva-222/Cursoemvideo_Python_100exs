from time import sleep
from random import randint
cont = 0
dado = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6),
        'Jogador5': randint(1, 6), 'Jogador6': randint(1, 6), 'Jogador7': randint(1, 6)}
print('Valores sorteados: ')
for c, v in dado.items():
    print(f'{c} tirou: {v}')
    sleep(0.5)
print('Ranking dos Jogadores: ')
for item in sorted(dado, key=dado.get, reverse=True):  #organiza o dicionário reverse pois organiza em ordem crescente
    print(f'{cont+1} Lugar: {item} com {dado[item]}')
    cont +=1
    sleep(0.5)
    if cont == 4:
        break








