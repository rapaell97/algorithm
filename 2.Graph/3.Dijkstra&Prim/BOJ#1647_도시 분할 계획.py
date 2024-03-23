import heapq

def prim(x):
    global ans
    queue = []
    V = [0] * (N + 1)
    heapq.heappush(queue, (0, x))

    while queue:
        temp, x = heapq.heappop(queue)

        if V[x]:
            continue

        V[x] = 1
        ans += temp
        lst.append(temp)

        for B, C in graph[x]:
            if V[B] == 0:
                heapq.heappush(queue, (C, B))

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

ans = 0
lst = []
prim(1)

print(ans-max(lst))
