# sen cos tan
import math
sct = float(input('Digite o ângulo que você deseja: '))
sin = math.sin(math.radians(sct))
cos = math.cos(math.radians(sct))
tan = math.tan(math.radians(sct))
print('O ângulo de {} graus tem o seno de {:.2f}'.format(sct, sin))
print('O ângulo de {} graus tem o cosseno de {:.2f}'.format(sct, cos))
print('O ângulo de {} graus tem a tangente de {:.2f}'.format(sct, tan))


