import sys
input = sys.stdin.readline
import heapq

def prim(n):
    global ans
    queue = []
    heapq.heappush(queue, (0, n))
    V = [0] * (N+1)

    while queue:
        cnt, com = heapq.heappop(queue)

        if V[com]:
            continue

        ans += cnt
        V[com] = 1

        for j in network[com]:
            if not V[j[0]] and j[0] != com:
                heapq.heappush(queue,(j[1], j[0]))


N = int(input())
M = int(input())
network = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    network[a].append((b, c))
    network[b].append((a, c))

ans = 0
prim(1)

print(ans)