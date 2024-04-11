import sys
sys.stdin = open('../../a.txt', 'r')
input = sys.stdin.readline
import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cnt, n = heapq.heappop(queue)

        if distance[n] < cnt:
            continue

        for v, w in graph[n]:
            temp = cnt + w

            if temp < distance[v]:
                distance[v] = temp
                heapq.heappush(queue, (temp, v))


V, E = map(int, input().split())
K = int(input())
INF = float('inf')
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])
