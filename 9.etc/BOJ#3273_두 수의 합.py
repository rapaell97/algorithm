N = int(input())
lst = list(map(int, input().split()))
X = int(input())

S, E = 0, N-1
cnt = 0
lst.sort()

while S < E:
    temp = lst[S] + lst[E]
    if temp == X:
        cnt += 1

    if temp < X:
        S += 1
    elif temp > X:
        E -= 1
    else:
        S += 1
        E -= 1

print(cnt)