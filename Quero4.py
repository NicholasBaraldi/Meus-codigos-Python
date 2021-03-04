V = int(input())
M = input()
coins = input().split(' ')
coins = list(map(int, coins))

i = 0

while i in range(0, M):
    while i in range(0, V):
        V = V - coins[i]