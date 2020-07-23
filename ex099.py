from time import sleep
# Função que identifica o maior número
def maior(lst):
    big = 0
    for y, x in enumerate(lst):
        print(x, end=' ')
        sleep(0.3)
        if lst[y] > big:        # Verfica se lst no indice y é maior que o maior número
            big = lst[y]
    print(f'Foram informados {len(lst)} valores ao todo')
    print(f'O maior valor encontrado foi {big}')
    print('='*30)
p, l, h, r, k = [1, 2, 3, 4, 5], [0, 0, 1, 2, 4, 2], [], [3, 3, 2, 2], [1, 800, 1, 2]
maior(l)
maior(p)
maior(h)
maior(r)
maior(k)

