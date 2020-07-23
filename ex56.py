# Analizador de dados
media = 0
maior = 0
vinte = 0
nome = ''
for c in range(1, 5):
    print('-'*20)
    print('{} Pessoa'.format(c))
    print('-'*20)
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).lower()
    media += i
    if c == 1 and s =='m':
        maior = i
        nome = n
    elif i > maior and s == 'm':
        maior = i
        nome = n
    if i < 20 and s == 'f':
        vinte += 1
print('A media das idades é {}'.format(media/4))
print('O homem mais velho detectado tem {} anos e  se chama {}'.format(maior, nome.capitalize()))
if vinte > 0:
    print('Ao todo foram detectadas {} mulheres com menos de 20 anos'.format(vinte))
else:
    print('Não foi detectada nenhuma mulher com menos de 20 anos')


