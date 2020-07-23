# Sequencia de fibonaci
pt = 0    # na sequencia de fibbonaci cada termo é igual aos dois termos anteriores somados!
st = 1     # a sequencia geralmente começa com 1 e 2 então eu declarei essas duas variaveis
c = 1      # declarei também um contador por estar usando while
n = int(input('Quantos termos você quer ver?'))
while not c == n+1:
    if c ==1:               # como o objetivo do programa é mostrar a sequencia em termos escolhidos caso seja a primeira vez que o while
        print('{}, {}'.format(pt, st), end='')  # roda ele escreverá os primeiros termos da sequencia
    else:       # Caso não seja ele ira rodar :
        ter = st + pt      # O terceiro termo da sequencia é igual a soma dos dois anteriores
        print('{},'.format(ter), end='')   # é necessario mostrar esse termo da sequencia e quando isso acaba
        pt = st     # pt recebe st então ele passa a ser um dos termos que ira ser somado com o outro para a obtençao do 4 termo
        st = ter    # st recebe ter pelo mesmo motivo
    c += 1          # incremento, agora o programa ira rodar novamente e com 2 termos atualizados
# 04/05/2020, olhei por cima uns comentários juro que não copiei xD


