def leia_money(msg):
    while True:
        n = str(input(f'{msg}'))
        nvn = validarnum(n)
        if nvn is False:
            print(f'\033[31m[ERRO] "{n}" não é um número válido, tente novamente\033[m')
        else:
            return nvn

def validarnum(p):
    """""
    :param p string a ser validada
    --> Função que detecta se o valor é númerico 
    --> Detecta mesmo com . e , ex: 1.000,00
    --> Detecta se: a virgulá está antes do ponto(caso isso ocorra return false)
    --> Aceita como número o valor que tiver um ponto a cada 3 valores
    --> Observação se no final do número após o ponto forem deixados menos ou mais de três algarismos ponto irá contar como virgula
    --> Considera valores sem ponto e virgula e nenhum  outro caractere a não ser . ou ,
    :return False se o valor digitado for inválido
    :return float do número caso ele for válido
    """""

    x = p.replace(',', '.').split('.')          # validação de ponto
    for c in range(0, len(x)):
        if c != 0 and c != len(x) - 1:
            if len(x[c]) != 3:
                return False
    if len(x) > 2 and len(x[0]) > 3:
        return False

    if '.' in p and ',' in p:    # Caso tenha virgula na frente de ponto
        if p.rfind('.') > p.rfind(','):
            return False

    x = p.replace('.', '').replace(',', '')  # validação do isnumeric (controlado)
    if x.isnumeric() is False:
        return False

    x = p.split(',')            # validação por qtd de virgulas
    if len(x) > 2:
        return False

    if '.' in p or ',' in p:        # Caso o número começe com virgula
        if p[0] == '.' or p[0] == ',':
            return False
        elif p[len(p) - 1] == ',' or p[len(p) - 1] == '.':
            return False

    # Retorno do número formatado apenas com o ponto da virgula
    virgula = False
    ponto = False
    virg = False
    if ',' in p:
        virgula = True
    if '.' in p:
        ponto = True
        x = p.split('.')
        if len(x) == 2:
            if len(x[1]) > 3 or len(x[1]) < 3:
                virg = True
    p = p.replace(',', '.').split('.')

    dcn = dict()
    cont = 0
    for c in p:
        dcn[cont] = c
        cont += 1
    dcn2 = dcn.copy()
    if virgula is True or ponto is True:
        for k, c in dcn2.items():
            if '.' in dcn[k]:
                del dcn[k]
        lend = len(dcn[len(dcn)-1])
        if lend !=3 or virgula is True or virg is True:
            dcn[len(dcn)-2] += '.'
    r = ''
    for k, c in dcn.items():
        r += dcn[k]
    return float(r)

def leianum(msg, mus=False):

    if mus is False:
        while True:
            try:
                num = int(input(msg))
            except (ValueError, TypeError):
                print('\033[31m[ERRO] o valor diigitado não é um número inteiro válido\033[m')
                break
            except KeyboardInterrupt:
                print('\033[31mO usuário preferiu não digitar esse número\033[m')
                num = 0
                break
            else:
                return num

