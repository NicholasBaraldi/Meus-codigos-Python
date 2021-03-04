V = int(input())
coins = input().split(' ')
coins = list(map(int, coins))
coins.sort(reverse=True)
# print(coins) # print para saber se o sort funcionou
total = V
totcoins = 0
m = len(coins)
i = 0
while i in range(0, m):
    if total >= int(coins[i]):
        total -= int(coins[i])
        totcoins += 1
    else:
        i += 1
print(totcoins)
