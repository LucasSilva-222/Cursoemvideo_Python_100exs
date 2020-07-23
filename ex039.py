from datetime import date
from playsound import playsound
a = int(input('Em que ano você nasceu? '))
s = str(input('Sexo (masculino ou feminino): ')).lower().strip()
ano = date.today().year
q = ano - a
print('Quem nasceu em {} tem {} anos em {}'.format(a, q, ano))

if q > 130:
    print('\033[4;31mSinto lhe informar mas o senhor(a) ja morreu!!!!!\033[m')
    playsound('ex39.mp3')
elif a > ano:
    print('Temos um \033[4;34mViagante do tempo AQUI\033[m')
elif q == 18 and s == 'masculino':
    print('Este ano você deve se apresentar ao \033[4;32mServiço Militar Obrigatório\033[m')
elif q > 18 and s == 'masculino':
    print('Caso não tenha se alistado, se aliste é \033[4;31mOBRIGATÓRIO\033[m')
    print('Você já deveria ter se alistado há {} anos'.format(ano - (a + 18)))
    print('Seu alistamento foi em {}'.format(a + 18))
elif s == 'feminino' and q >= 18:
    print('Serviço militar \033[4;30mNÃO OBRIGATÓRIO\033[m tenha um bom dia!')
elif q < 18 and 'feminino' in s or 'masculino' in s:
    print('Menores não se alistam no exercito')
    print('Ainda faltam {} anos!'.format(18-q))
    print('Seu alistamento será em {}'.format((18 - q) + ano))
else:
    print('Os dados inseridos são invalidos!')




















