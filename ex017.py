# h2 = ca2 + co2
import math
Ca = int(input('Cateto adjacente (metros): '))
Co = int(input('Cateto oposto(metros): '))
hip = math.hypot(Ca, Co)
print('A hipotenusa mede {:.2f} metros '.format(hip))
