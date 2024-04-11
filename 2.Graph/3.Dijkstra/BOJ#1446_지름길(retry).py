import sys

sys.stdin = open('../../a.txt', 'r')

N, D = map(int, input().split())
lst = []

for _ in range(N):
    a, b, c = map(int, input().split())
    lst.append((a, b, c))

dist = [i for i in range(D + 1)]

for i in range(D + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)

    for s, e, d in lst:
        if s == i and e <= D and dist[i] + d < dist[e]:
            dist[e] = dist[i] + d

print(dist[D])
