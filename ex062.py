# PA com while v2 Ultra
n = int(input('Digite o primeiro termo da PA:'))
n2 = int(input('Digite a razão da PA:'))
t = 1
d = n +(10-1)*n2
while n <= d:
    print('{} termo = {} '.format(t, n))
    t +=1
    n += n2
d = 1
t = 11
n3 = 1
while n3 != 0:
    n3 = int(input('Quantos termos a mais você quer ver? '))
    en = n +(n3-1)*n2
    if n3 >0:
        while n <= en:
            print('{} termo = {}'.format(t, n))
            t += 1
            n += n2
print('Programa encerrado com um total de {} termos mostrados'.format(t-1))















