dcn = dict()
gols = list()       # inicia uma lista e um dicionário
b = 0
dcn['nome'] = str(input('Qual o nome do jogador? '))    # para a key nome pergunta o nome do jogador
partidas = int(input('Quantas partidas ele jogou?'))    # Pergunta o total de partidas que ele jogou
for c in range(1, partidas+1):      # Pergunta o tando de gols que ele fez em cada partida que ele jogou
    gol = int(input(f'Quantos gols na partida {c}: '))
    gols.append(gol)        # Adiciona esse valores a uma lista
    b += gol            # Conta qtd de gols feitos somados
dcn['Gols'] = gols[:]       # Adiciona os valores da lista e dos gols ao dicionário
dcn['Total'] = b
print(f'O jogador {dcn["nome"]} jogou {partidas} partida(s)')
for a in range(0, len(dcn['Gols'])):
    print(f'Na partida {a+1} fez {dcn["Gols"][a]} gol(s)')
print(f'Um total de {dcn["Total"]} gols marcados')


