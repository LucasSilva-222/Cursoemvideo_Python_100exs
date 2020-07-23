dcn = dict()
info = list()
tot = list()        # iniciei 1 dicionários e 2 lista
while True:
    total = 0       # variavel total para calular o total de gols criada(no inicio do while para resetar a cada repetição)
    dcn['nome'] = str(input('Qual o nome do jogador? ')).capitalize()       # Pergunta o nome e o coloca  em uma key de mesmo nome
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(1, partidas+1):      # +1 pois o for ignora o ultimo número
        tot.append(int(input(f'Quantos gols na partida {c}?:')))        # é adicionado na lista cada gol que o jogador fez nas partidas que jogou
        total += tot[c-1]       # o total de gols é feito c-1 pois o indicie de contagem desse for começa com 1
    dcn['total'] = total        # o total de gols é adicionado no dicionário
    dcn['gols'] = tot[:]         # A mesma coisa ocorre com os gols (copia da lista para não dar problema)
    info.append(dcn.copy())             # Após esse processo os dados são colocados na lista info
    dcn.clear()     # e as outras  são resetadas para que sejam inseridas novamnete em outro indicie de info
    tot.clear()
    while True:
        choise = input(str('Quer continuar?[S/N]')).lower()
        if choise == 's' or choise == 'n':          #  o famoso esquema do quer continuar
            break
    if choise == 'n':
        break
print('='*60)
for x, y in enumerate(info):            # aqui x vira um indicie e y um dicionario com todas as keys dessa maneira esse for irá fazer esse processo até len de info - 1
    print(f'Número: {x}  Nome: {y["nome"]} Gols: {y["gols"]:}  Total: {y["total"]}')
    print('='*60)
while True:
    choise2 = int(input('Ver dados de qual jogador? (999)Encerra'))     # aqui  é perguntado qual jogador será visto os dados
    if choise2 == 999:      # por fim o esquema de flag ufa :)
        break
    if choise2 > len(info)-1 or choise2 < 0:        # se o número do jogador for valido ou seja estar dentro dos números que estão dentro de info o programa irá seguir caso contrário ele ira dizer que não encontroi o usuário
        print('Número não cadastrado')
    else:
        print(f'Levantamento do jogador {info[choise2]["nome"]}')
        for a in range(0, len(info[choise2]["gols"])):          # aqui crei um for que vai de 0 até o len de info-1 no for é informado cada gol que o jogador fez na partida
            print(f'Partida {a+1}: {info[choise2]["gols"][a]} gols.')   #a+1 pois coemeça no 0 choise o indicie do jogador que quer ser visto goals pois queremos ver o gol e a para ver o gol feito naquela partida
print('='*60)


















