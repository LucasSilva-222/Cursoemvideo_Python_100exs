# Validador de dados
n = str(input('Digite o seu sexo [M/F] ')).upper()
while 'F' != n != 'M':
    n = str(input('Dado inválido, por favor insira seu sexo [M/F] ')).upper()
if n == 'M':
    print('Sexo Masculido registrado com sucesso!!!')
elif n == 'F':
    print('Sexo Feminino registrado com sucesso!!!')
