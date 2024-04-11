import heapq

def prim(n):
    global ans

    queue = []
    V = [0] * N
    heapq.heappush(queue, (0, n))

    while queue:
        dist, star = heapq.heappop(queue)

        if V[star]:
            continue

        ans += dist
        V[star] = 1
        x, y = graph[star]
        for j in range(N):

            if not V[j]:
                nx, ny = graph[j]
                if x == nx:
                    temp = abs(ny - y)

                elif y == ny:
                    temp = abs(nx - x)

                else:
                    temp = (((x - nx) ** 2) + ((y - ny) ** 2)) ** 0.5

                heapq.heappush(queue,(temp, j))


N = int(input())
graph = []

for i in range(N):
    x, y = map(float, input().split())
    graph.append((x, y))

ans = 0
prim(0)

print(round(ans, 2))
