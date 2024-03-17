import sys
sys.stdin = open('../../a.txt', 'r')
import heapq

def dijkstra(i, k):
    queue = []
    heapq.heappush(queue,(0, i, k))
    break_lst[i][k] = 0

    while queue:
        cnt, i, k = heapq.heappop(queue)

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0<= ni <N and 0<= nk <M:
                temp = cnt + float(lst[ni][nk])
                if break_lst[ni][nk] > temp:
                    break_lst[ni][nk] = temp
                    heapq.heappush(queue,(temp, ni, nk))


M, N = map(int, input().split())
INF = float('inf')

lst = [list(input()) for _ in range(N)]
break_lst = [[INF] * M for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

dijkstra(0, 0)
print(int(break_lst[N - 1][M - 1]))