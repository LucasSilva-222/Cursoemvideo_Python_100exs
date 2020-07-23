from datetime import date
ano = date.today().year     # Comado que pega a hora do computador
dici = dict()
dici['Nome'] = str(input('Nome: '))
dici['Idade'] = ano - int(input('Ano de nascimento: '))
dici['Ctps'] = input('Carteira de trabalho (0 não tem)')
if dici['Ctps'] != '0':
    dici['Contratação'] = int(input('Ano de contratação: '))
    dici['Salário'] = input('Salário: ')
    if ano - dici['Contratação'] <= 35:
        dici['Aposentadoria'] = (dici['Idade'] + dici['Contratação'] + 35) - ano
    else:
        dici['Aposentadoria'] = 'Já pode aposentar'
for k, v in dici.items():
    print(f'{k} tem o valor {v}')
