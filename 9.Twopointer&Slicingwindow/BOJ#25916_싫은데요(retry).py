N, M = map(int, input().split())
lst = list(map(int, input().split()))

S, E, ans, temp = 0, 0, 0, 0 

while E < N:
    if temp + lst[E] <= M:
        temp += lst[E]
        E += 1
        ans = max(ans, temp)
    else:
        temp -= lst[S]
        S += 1

print(ans)