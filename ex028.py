# Jogo da Adivinhação
from random import randint
from playsound import playsound
a = randint(0, 5)   # Número aleatório de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5 tente adivinhar')
print('-=-' * 20)
ap = int(input('Insira Aqui: '))
if ap == a:
    print('Você acertou!!!')
    playsound('2ex028.mp3')
else:
    print('Ah você errou tente denovo!')
    playsound('ex028.mp3')
print('O numero correto é {}'.format(a))










