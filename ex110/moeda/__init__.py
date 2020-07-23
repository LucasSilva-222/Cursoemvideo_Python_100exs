def medade(num, frmt=False):  # Em todas as funções as contas de seus respectivos nomes é feita
    valor = num / 2
    return moeda(
        valor) if frmt else valor  # Em todas as funções o parametro frmt for == true ele ira mostrar com a formatação de real através da ultima função


def dobro(num, frmt=False):
    valor = num * 2
    return moeda(valor) if frmt else valor


def aumentar(num, porcentagem, frmt=False):
    valor = (num * (porcentagem / 100)) + num
    return moeda(valor) if frmt else valor


def diminuir(num, porcentagem, frmt=False):
    valor = num - (num * (porcentagem / 100))
    return moeda(valor) if frmt else valor


def moeda(num):                   # A função moeda(num)
    return str(f'{num:.2f}R$').replace('.', ',')


def resumo(n, aumento, reducao):
    print('-'*30)
    print(' Resumo do valor '.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{n}')
    print(f'Dobro do preço: \t{dobro(n, frmt=True)}')
    print(f'Aumento de {aumento}%: \t{aumentar(n, aumento, frmt=True)}')
    print(f'Redução de {reducao}%: \t{diminuir(n, reducao, frmt=True)}')


