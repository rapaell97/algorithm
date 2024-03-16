import heapq


def dijkstra(i, k):
    queue = []
    cnt = 0
    heapq.heappush(queue, (cnt, i, k))

    while queue:
        cnt, i, k = heapq.heappop(queue)
        if i == N and k == N:
            return

        if cnt > cost[i][k]:
            return

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0 <= ni < N and 0 <= nk < N:
                temp = cnt + lst[ni][nk]
                if temp < cost[ni][nk]:
                    cost[ni][nk] = temp

                    heapq.heappush(queue, (temp, ni, nk))

N = int(input())
lst = [list(input()) for _ in range(N)]

for i in range(N):
    for k in range(N):
        if lst[i][k] == '1':
            lst[i][k] = 0
        else:
            lst[i][k] = 1

di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]
INF = float('inf')
cost = [[INF] * N for _ in range(N)]

dijkstra(0, 0)
print(cost[N-1][N-1])
