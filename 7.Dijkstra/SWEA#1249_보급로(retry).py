import heapq
import sys
sys.stdin = open('../a.txt', 'r')

di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]


def dijkstra(i, k, cnt):
    queue = []
    heapq.heappush(queue, (i, k, cnt))

    while queue:
        i, k, cnt = heapq.heappop(queue)
        if i == N - 1 and k == N - 1:
            return

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0<= ni <N and 0<= nk <N:
                temp = cnt + lst[ni][nk]

                if distance[ni][nk] > temp:
                    distance[ni][nk] = temp

                    heapq.heappush(queue, (ni, nk, temp))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]

    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0

    dijkstra(0, 0, 0)
    print(f"#{tc} ", distance[N-1][N-1])
