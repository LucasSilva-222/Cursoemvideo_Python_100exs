lista = []  # iniciei uma lista vazia
for c in range(0, 5):   # O for irá repidir 5 vezes para ler 5 números
    n = int(input('Digite um número: '))
    if c == 0:                  # Caso o c seja 0 o número so pode ser adcionado na posição 0 pois é o começo a 1 vez
        lista.insert(c, n)
        print('Adicionado a posição: 0')
    elif c == 1:            # caso for 1 serão 2 valores que teram sido lidos
        if n >= lista[c-1]:     # se n for maior que 0 (c-1) ele sera colocado na posição 1
            lista.insert(c, n)
            print('Adicionado a posição: 1')
        else:               # se ele não for maior será colocado na posição 0 (c-1)
            lista.insert(c-1, n)
            print('Adicionado a posição: 0')
    elif c >= 2:        # a partir do momento em que temos mais de 2 valores sendo lidos é necessário verificar se n é maior ou menor do que os outros números
        for x in range(0, len(lista)):              # x vira um indicie neste caso ele vai até  o comprimento de lista no momento
            if n == lista[x]:           # é verificado se existe um número repitido, caso exista ele sera colocado na mesma posição que o seu duplicado
                lista.insert(x, n)
                print(f'Adicionado na posição {x}')
                break
            if lista[x+1] > n > lista[x]:          # aqui é verificado se n está entre 2 números da lista (o for é necessário para aumentar o indicie do x caso ele não atenda as condições)
                lista.insert(x+1, n)                # ele é colocado na pocisção x+1 pois o x+1 que foi testado é maior que n, e esse valor será colocado uma posição a frente
                print(f'Adicionado a posição: {x+1}')
                break
            elif n > max(lista):        # aqui é verificado se n é maior do que o maior número da lista
                lista.insert(lista.index(max(lista))+1, n)  #ele é colocado na posição a frente do maior número e como consequencia é necessário colocar o +1 pois queremos colocalo em uma pocisão superior e não substituir
                print(f'Adicionado no final da lista')
                break
            elif n < min(lista):        # O mesmo é feito para o valor minimo só que não é preciso colocar +1 pois se ele é menor que o menor, ele deve ocupar o começo da lista
                lista.insert(lista.index(min(lista)), n)
                print(f'Adicionado ao começo da lista ')
                break           # o break é necessário pois são adicionadas novos indicies e o len de lista sempre aumenta tornando o for um while True. quando a condição é atendida não existe a neceesidade de continuar com o for
print(f'Em ordem os números digitados foram {lista}')
