# Aprovado, Reprovado, Recuperação
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunta nota: '))
m = (n1+n2)/2


if m >10 or n1 > 10 or n2 > 10 or n1 < 0 or n2 < 0:
    print('\033[4;35mMédia invalida!\033[m verifique os números digitados')
elif m < 5:
    print('\033[4;31mREPROVADO\033[m')
    print('Sua média foi \033[31m {}\033[m'.format(m))
elif 7 > m >= 5:
    print('\033[4;37mRECUPERAÇÃO\033[m')
    print('Sua média foi \033[4;37m{}\033[m'.format(m))
else:
    print('\033[34mAPROVADO\033[m')
    print('Sua média foi \033[4;34m{}\033[m'.format(m))










