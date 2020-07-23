#Soma de números com flag
n = 0
c = 0
v = 0
while n != 999:
    n = int(input('Digite um numero para parar [999]: '))
    if n != 999:
        c += n
        v +=1
print('A soma dos {} valores digitados (desconciderando 999) é igual a {}'.format(v, c))
