def find(n):
    if p[n] != n:
        p[n] = find(p[n])
    return p[n]


def union(n, m):
    n = find(n)
    m = find(m)

    if n == m:
        return
    if n < m:
        p[m] = n
    else:
        p[n] = m

import sys
sys.stdin = open('../../a.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    p = [0] + list(range(1, N + 1))

    for i in range(0, 2 * M, 2):
        union(lst[i], lst[i+1])

    for i in range(1, N+1):
        find(i)

    print(f"#{tc} {len(set(p))-1}")
