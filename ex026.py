# Detector de A
A = input('Digite uma frase: ').strip().lower()
print('A letra a aparece {} vezes'.format(A.count('a')))
print('A Letra a aparece pela primeira vez na posição {}'.format(A.find('a')+1))
print('A Letra a aparece pela ultima vez vez na posição {}'.format(A.rfind('a')+1))


