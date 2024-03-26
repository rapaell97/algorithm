G = int(input())
E = 1
S = 1

check = False
while True:
    temp = E ** 2 - S ** 2
    if temp == G:
        check = True
        print(E)
        E += 1
    elif temp > G:
        S += 1
    else:
        E += 1

    if S >= E:
        break


if not check:
    print(-1)
