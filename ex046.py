# Fogos de artifício.
from playsound import playsound
from time import sleep
for c in range(10, -1, -1):
    print('\033[4m{}\033[m!'.format(c))
    sleep(1)
print('\033[4;32mFELIZ ANO NOVO!!!!!')
playsound('somex046.mp3')
