# 10 primeiros termos de uma PA
print('='*23)
print('{:^20}'.format('10 primeiros termos PA'))
print('='*23)

n1 = int(input('Digite o primeiro termo da PA:'))
n2 = int(input('Digite a razão da PA:'))
d = n1 + (10-1)*n2
t = 1
for c in range(n1, d + 1, n2):
    print('Termo {} = {}'.format(t, c))
    t += 1
