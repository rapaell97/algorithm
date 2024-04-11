import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open('a.txt', 'r')
input = sys.stdin.readline
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    elif x < y:
        p[y] = x

    else:
        p[x] = y


N, M = map(int, input().split())
p = list(range(N+1))

for _ in range(M):
    o, a, b = map(int, input().split())

    if o == 0:
        union(a, b)

    else:
        pa = find(a)
        pb = find(b)

        if pa == pb:
            print('YES')

        else:
            print('NO')

