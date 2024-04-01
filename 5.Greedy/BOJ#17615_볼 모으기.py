def funcL(C):
    check = 0
    temp = 0
    for i in range(N):
        if lst[i] != C:
            check = 1

        if check and lst[i] == C:
            temp += 1

    return temp

def funcR(C):
    check = 0
    temp = 0
    for i in range(N - 1, -1, -1):
        if lst[i] != C:
            check = 1

        if check and lst[i] == C:
            temp += 1

    return temp

N = int(input())
lst = list(input())

ans = 0
print(min(funcL('R'), funcR('R'), funcL('B'), funcR('B')))

