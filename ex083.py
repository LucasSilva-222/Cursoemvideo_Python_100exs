p = str(input('Digite uma expressão matemática: '))
if '(' not in p or ')' not in p:
    print('Expressão inválida')
elif p.index('(') < p.index(')'):
    if p.count('(') == p.count(')'):
        print('Sua expressão é válida')
    else:
        print('Sua expressão é inválida')
else:
    print('Expressão inválida')




