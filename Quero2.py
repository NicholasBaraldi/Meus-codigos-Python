P1 = input()
P2 = input()

P1 = list(P1)
P2 = list(P2)

P1.sort()
P2.sort()

m = len(P1)

i = 0

for i in range(0, m):
    if P1[i] == P2[i]:
        i += 1
        if i == m:
            print("true")
    else:
        print("false")
        break
