import sys
sys.stdin = open('../a.txt', 'r')

M, N = map(int, input().split())
lst = list(map(int, input().split()))

S, E = 1, max(lst)
ans = 0
while S <= E:
    mid = (S + E) // 2

    temp = 0
    for i in lst:
        temp += (i // mid)

    if temp >= M:
        S = mid + 1
        ans = mid

    else:
        E = mid - 1

print(ans)
