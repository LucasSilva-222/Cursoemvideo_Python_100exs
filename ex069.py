# Analizador de dados
c = ''
end = 1
m = 0
mc = 0
mm = 0
while True:
    saida = 0
    s = ''
    i = int(input('Informe a idade: '))
    while 'm' != s != 'f':
        s = input('Informe o sexo [M / F]: ').lower()
    if i >= 18:
        m += 1
    if s == 'm':
        mc += 1
    elif s == 'f' and i < 20:
        mm += 1
    while True:
        c = input('Quer continuar??[S/N]: ').lower()
        if c == 's':
            break
        elif c == 'n':
            saida = 1
            end = 0
            break
    if end == 0:
        break
print(f'Ao todo {m} pessoas tem mais de 18 anos, {mc} homens foram cadastrados e {mm} mulheres foram registradas com menos de 20 anos! ')

