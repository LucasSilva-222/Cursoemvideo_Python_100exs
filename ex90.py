situacao = dict()
situacao['Nome'] = str(input('Qual o nome do aluno?')).capitalize()
situacao['Media'] = float(input('Qual a média do aluno?'))
if situacao['Media'] >= 7.0:
    situacao['Situação'] = 'Aprovado'       # Condições para adicionar um item ao dicionário.
elif 6.9 >= situacao['Media'] >= 5.0:
    situacao['Situação'] = 'Recuperação'
else:
    situacao['Situação'] = 'Reprovado'
for k, v in situacao.items():
    print(f'{k} é igual a {v}')


