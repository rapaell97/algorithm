import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
ans = 2000000000

S, E = 0, 0
while S < N - 1:
    temp = lst[E] - lst[S]
    if temp >= M:
        ans = min(ans, temp)
        S += 1
        E = S

    else:
        E += 1

        if E == N:
            S += 1
            E = S

print(ans)
