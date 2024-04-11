import heapq

def dijkstra(s, dist):
    queue = []
    heapq.heappush(queue,(0, s))

    while queue:
        d, s = heapq.heappop(queue)

        if dist[s] < d:
            continue

        for e, w in graph[s]:
            temp_d = d + w
            if temp_d < dist[e]:
                dist[e] = temp_d
                heapq.heappush(queue,(temp_d, e))


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

INF = float('inf')
dist_1 = [INF] * (N + 1)
dist_2 = [INF] * (N + 1)

ans = 0
dijkstra(X, dist_2)
for i in range(1, N+1):
    if i != X:
        dist_1 = [INF] * (N + 1)
        dijkstra(i, dist_1)
        ans = max(ans, dist_2[i] + dist_1[X])

print(ans)



