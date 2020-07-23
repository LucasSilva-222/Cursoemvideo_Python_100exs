# ELIF AUMENTO
sal = float(input('Quanto você ganha? '))
if sal <= 1250.00:
    al = sal * 0.15
    print('Seu salário teve um aumento de 15% agora você ganha {}R$'.format(sal + al))
elif sal > 1250.00:
    al2 = sal * 0.10
    print('Seu salário teve um aumento de 10% agora você ganha {}R$'.format(sal + al2))



