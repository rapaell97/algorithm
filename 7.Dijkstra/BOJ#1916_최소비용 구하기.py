import sys
sys.stdin = open('../a.txt', 'r')
import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0, start))
    distance[start] = 0

    while queue:
        cnt, n = heapq.heappop(queue)

        if cnt > distance[n]:
            continue

        for v, w in graph[n]:
            temp = cnt + w

            if distance[v] > temp:
                distance[v] = temp
                heapq.heappush(queue, (temp, v))


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
INF = float('inf')
distance = [INF] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

S, E = map(int, input().split())
dijkstra(S)
print(distance[E])
