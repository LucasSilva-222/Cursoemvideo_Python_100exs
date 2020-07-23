# detector de vogais
tp = ('OLA', 'LUCAS', 'LINDO', 'DEMAIS', 'PROGRAMA', 'QUE', 'LEI', 'VOGAIS', 'TESTE')
vogais =('A', 'E', 'I', 'O', 'U')
for c in range(0, len(tp)):
    print(f'A palavra {tp[c]} tem essas vogais:', end='')
    for letra in tp[c]:
        if letra in 'AEIOU':
            print(letra, end='')
    print('\n')
