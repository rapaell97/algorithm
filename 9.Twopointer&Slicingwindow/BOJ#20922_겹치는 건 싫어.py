import sys
sys.stdin = open('../a.txt', 'r')

N, K = map(int, input().split())
lst = list(map(int, input().split()))
C = [0] * (max(lst) + 1)

ans, S, E = 1, 0, 0
while S <= E and E < N:
    if C[lst[E]] < K:
        C[lst[E]] += 1
        ans = max(E - S + 1, ans)
        E += 1

    else:
        C[lst[S]] -= 1
        S += 1

print(ans)