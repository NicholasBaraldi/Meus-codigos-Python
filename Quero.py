N = int(input())
A = input().split(' ')
A = list(map(int, A))

i = 1

while i in range(1, N+1):
    if i not in A:
        break
    else:
        i += 1
print(i)
