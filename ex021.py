# Tocar arquivo mp3 MELHORADO
from pygame import mixer  # Importa o mixer da bibilioteca pygame
import time
n = str(input('hit the road?: ')).strip().lower()

if n == 'jack':
    mixer.init()
    mixer.music.load('ex021.mp3')  # Carrega o arquivo mp3
    mixer.music.play()  # Toca o arquivo
    time.sleep(360)
else:
    mixer.init()
    mixer.music.load('2ex021.mp3')  # Carrega o arquivo mp3
    mixer.music.play()  # Toca o arquivo
    time.sleep(2)





