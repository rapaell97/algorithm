import heapq

def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n))

    while queue:
        cnt, n = heapq.heappop(queue)

        if cnt > lst[n]:
            continue

        for e, f in graph[n]:
            temp = cnt + f
            if temp < lst[e]:
                parent[e] = n
                lst[e] = temp
                heapq.heappush(queue, (temp, e))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(M)]
    for _ in range(N):
        s, e, f = map(int, input().split())
        graph[s].append((e, f))
        graph[e].append((s, f))

    INF = float('inf')
    lst = [INF] * M
    parent = [0] * M

    dijkstra(0)

    E = M-1
    path = [E]
    while E != 0:
        E = parent[E]
        path.append(E)

    if lst[-1] == INF:
        print(f"Case #{tc}: {-1}")
    else:
        print(f"Case #{tc}:", *path[::-1])