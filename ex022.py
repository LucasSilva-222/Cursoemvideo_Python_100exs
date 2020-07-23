# Analizador de textos
frase = str(input('Insira seu nome completo: '))
print('Seu nome com letras MAIÚSCULAS: {}'.format(frase.upper()))
print('Seu nome com letras minúsculas: {}'.format(frase.lower()))
e = frase.count(' ')  # conta os espaços
t = len(frase)
se = t - e
print('Seu nome tem {} carácteres'.format(se))
dv = frase.split()
print('Seu primeiro nome tem {} carácteres'.format(len(dv[0])))

