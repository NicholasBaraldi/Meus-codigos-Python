N = int(input())

while N != 0:
    P = int(input())
    soma = 0
    while P != 0:
        Q, V = map(int, input().split(' '))
        soma += Q*V
        P -= 1
    D = int(input())
    troco = D - soma

    if troco < 0:
        print('DINHEIRO INSUFICIENTE')
    else:
        print(troco)
    N -= 1
