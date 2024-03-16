import heapq
import sys
sys.stdin = open('../a.txt', 'r')
def dijkstra(i, k):
    queue = []
    cnt = lst[0][0]
    heapq.heappush(queue, (cnt, i, k))

    while queue:
        cnt, i, k = heapq.heappop(queue)

        if cnt > cost[i][k]:
            return

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni <N and 0<= nk <N:
                temp = cnt + lst[ni][nk]
                if cost[ni][nk] > temp:
                    cost[ni][nk] = temp
                    heapq.heappush(queue, (temp, ni, nk))

T = 1
while True:
    N = int(input())
    if N == 0:
        break

    lst = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    cost = [[INF] * N for _ in range(N)]

    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]

    dijkstra(0, 0)
    print(f"Problem {T}: {cost[N-1][N-1]}")
    T += 1