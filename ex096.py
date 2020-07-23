# Função que calcula  area
def area(a, b):
    print(f'A área do seu terreno de {a}X{b} é de {a*b} metros quadrados')
x = float(input('Qual a largura do terreno(m) '))
y = float(input('Qual o comprimento do terreno?(m) '))
area(x, y)      # Os valores de x e y viram a e b quando a função area é chamada

