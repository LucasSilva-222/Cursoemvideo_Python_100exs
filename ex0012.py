# 5% de desconto
n = int(input('Qual o preço atual do produto? '))
desconto = n * 0.05
print('Desconto de 5%!!\nDe {}R$ por apenas {:.2f}R$ !!'.format(n, n-desconto))
