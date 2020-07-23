# PA com while
n = int(input('Digite o primeiro termo da PA:'))
n2 = float(input('Digite a razão da PA:'))
t = 1
d = n +(10-1)*n2
while n <= d:
    print('{} termo = {}'.format(t, n))
    t +=1
    n += n2
