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

N = int(input())
p = [0] + list(range(1, N + 1))

for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N+1):
    find(i)

sp = set(p[1:])
ans = list(sp)
print(*ans[:2])