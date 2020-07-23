# Detector de maioridade v2
from datetime import date
s = 0
ano = date.today().year
for c in range(1, 8):
    n = float(input('Digite uma data de nascimento [{} de 7]: '.format(c)))
    idade = ano - n
    if idade >= 18:
        s = s+1
c = 7 - s
print('Identificamos que {} dessas pessoas são menores e {} já atingiram a maioridade!  '.format(c, s))
