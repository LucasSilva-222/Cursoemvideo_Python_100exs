# Print adaptado com o texto
def pstyle(msg):
    print('='*len(msg))         # printa = de acordo com o tamando do texto digitado
    print(msg)
    print('='* len(msg))
g = str(input('Digite uma frase: '))
pstyle(g)
