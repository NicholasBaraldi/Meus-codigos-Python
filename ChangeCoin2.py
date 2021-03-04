coins = input().split(' ')
V = int(input())
total = V
totcoins = 0
m = len(coins)
i = m - 1
while i >= 0:
    if total >= int(coins[i]):
        total -= int(coins[i])
        totcoins += 1
    else:
        i -= 1
print(totcoins)
