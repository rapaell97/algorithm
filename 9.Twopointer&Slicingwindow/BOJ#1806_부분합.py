N, M = map(int, input().split())
lst = list(map(int, input().split()))

S, E = 0, 0
cnt = N
temp = lst[S]
check = False
while E <= N-1:

    if temp >= M:
        cnt = min(cnt, len(lst[S:E+1]))
        temp -= lst[S]
        S += 1
        check = True

    elif temp < M:
        E += 1

        if E >= N:
            break
        temp += lst[E]

if check:
    print(cnt)
else:
    print(0)