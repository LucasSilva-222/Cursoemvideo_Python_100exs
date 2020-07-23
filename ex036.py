# Aprovação de emprestimo
cas = float(input('Qual o valor da casa? '))
sal = float(input('Qual sua renda mensal? '))
an = float(input('Em quantos anos você irá parcelar? '))
am = an * 12
par = cas / am
s = sal * 0.30
print('Para pagar uma casa de {}R$ em {} anos, são necessárias parcelas mensais de {:.2f}R$'.format(cas, an, par,))
if par <= s:
    print('\033[32mEmprestimo aprovado\033[m')
elif par > s:
    print('\033[31mEmprestimo negado\033[m')
    print('Motivo: O valor exedeu 30% do salário do solicitante')
print('\033[34mTenha um bom dia!\033[m')







