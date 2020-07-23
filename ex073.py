# Tabela Brasileirão 2018
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atletigo-MG', 'Atletico-PR', 'Cruzeiro', 'Botafogo')
times2 = ('Santos', 'Bahia', 'Fluminence', 'Corinthians', 'Chapecoence', 'Ceará', 'Vasco', 'Sport', 'America-MG', 'Vitória', 'Paraná')
todos = times + times2
print('-'* 20)
print(f'Lista de times serie A Brasileirão: {todos}')
print('-'* 20)
print(f'Os 4 primeiros colocados são: {todos[:5]}')
print('-'* 20)
print(f'Os 4 ultimos são: {todos[16:]}')
print('-'* 20)
print(f'Times em ordem alfabetica: {sorted(todos)}')
print('-'* 20)
pos = 0
team = str(input('Qual time você quer ver a pocição?')).strip()
for c in todos:
    if team in c:
        pos += 1
        break
    else:
        pos += 1
print(f'{team} está na {pos}ª posição')
