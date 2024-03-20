import sys

sys.stdin = open('../a.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 0
V = [0] * N
for i in range(N):
    target = lst[i]
    S = 0
    E = N - 1
    while S < E:
        if S == i:
            S += 1
            continue
        elif E == i:
            E -= 1
            continue

        temp = lst[S] + lst[E]
        if temp == target and V[i] == 0:
            V[i] = 1
            ans += 1
            break
        if temp > target:
            E -= 1
        else:
            S += 1
print(ans)
