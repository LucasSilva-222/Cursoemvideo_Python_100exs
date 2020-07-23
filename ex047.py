# pares entre 1 e 50
from time import sleep
print('-=-'*20)
print('{:^60}'.format('Pares de 1 à 5'))
print('-=-'*20)
v = 0
for c in range(1, 51):
    if v % 2 == 0:
        print('O número \033[37m{}\033[m é par e está entre 1 e 50!'.format(v))
        sleep(0.2)
        v = v + 1
    else:
        v = v +1
