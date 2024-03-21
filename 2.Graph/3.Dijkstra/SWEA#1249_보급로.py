import heapq

di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]


def dijkstra(i, k):
    queue = []
    heapq.heappush(queue, (0, i, k))

    while queue:
        cnt, i, k = heapq.heappop(queue)

        if cnt > distance[i][k]:
            continue

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0 <= ni < N and 0 <= nk < N:
                temp = cnt + lst[ni][nk]

                if distance[ni][nk] > temp:
                    distance[ni][nk] = temp
                    heapq.heappush(queue, (temp, ni, nk))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]

    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0

    dijkstra(0, 0)
    print(f"#{tc} ", distance[N - 1][N - 1])
