# Desconto se viajar mais
print('{:=^50}'.format('Seja Bem Vindo'))
n = float(input('Quantos quilometros você percorerá ate o destino? '))
if n > 200:
    p = n * 0.45
    print('A passagem custa {}R$'.format(p))
else:
    p2 = n * 0.50
    print('A viagem ira custar {}R$'.format(p2))


