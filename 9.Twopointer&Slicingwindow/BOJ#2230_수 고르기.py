import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
ans = 2000000000

S, E = 0, 0
while S <= E and E < N:
    temp = lst[E] - lst[S]
    if temp >= M:
        ans = min(ans, temp)
        S += 1
    else:
        E += 1

print(ans)
