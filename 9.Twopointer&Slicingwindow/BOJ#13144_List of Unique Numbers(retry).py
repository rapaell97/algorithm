import sys

sys.stdin = open('../a.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))
check = [0] * (1000001)
S, E = 0, 0
ans = 0

while S <= E and E < N:
    if not check[lst[E]]:
        check[lst[E]] = 1
        E += 1
        ans += (E - S)

    else:
        check[lst[S]] = 0
        S += 1

print(ans)
