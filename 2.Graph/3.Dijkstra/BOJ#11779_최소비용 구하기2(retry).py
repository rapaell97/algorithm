import heapq


def dijkstra(S):
    queue = []
    heapq.heappush(queue, (0, S))

    while queue:
        cnt, S = heapq.heappop(queue)

        if cnt > cost[S]:
            continue

        else:
            for c, e in graph[S]:
                temp = cnt + c
                if cost[e] > temp:
                    cost[e] = temp
                    path[e] = S
                    heapq.heappush(queue, (temp, e))


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))

S, E = map(int, input().split())

INF = float('inf')
cost = [INF] * (N + 1)
cost[S] = 0

path = [[] for _ in range(N + 1)]
path[S] = [S]

dijkstra(S)
print(cost[E])

ans_lst = [E]
while E != S:
    E = path[E]
    ans_lst.append(E)
print(len(ans_lst))
print(*ans_lst[::-1])
