# conversão
n = int(input('Digite um número: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
n2 = int(input('Selecione: '))
if n2 == 1:
    print('{} Convertido para BINÁRIO é igual a {} '.format(n, bin(n)[2:]))
elif n2 == 2:
    print('{} Convertido para OCTAL é {} '.format(n, oct(n)[2:]))
elif n2 == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(n, hex(n)[2:]))
else:
    print('Opção Inválida!!! ')



