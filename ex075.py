# Analisador de dados tupla
tp = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite o penultimo número: ')), int(input('Ultimo número: ')))
print(f'O valor 9 apareceu {tp.count(9)} vezes' if 9 in tp else 'O valor 9 não apareceu')
print(f'O primeiro valor três aparece na pocição {tp.index(3)+1}' if 3 in tp else '3 não foi encontrado')
print('Os valores pares digitados foram: ', end='')
for c in range(0, len(tp)):
    x = tp[c]
    if x % 2 == 0:
        print(f'{x} ', end='')


