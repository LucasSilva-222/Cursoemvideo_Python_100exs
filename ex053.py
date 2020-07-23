# Detector de palíndromo
n = input('Digite uma frase: ').upper().replace(' ', "")
if n == n[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
print('O inverso de {} é {}'.format(n, n[::-1]))
