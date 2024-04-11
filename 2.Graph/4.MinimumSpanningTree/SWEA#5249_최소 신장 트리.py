import heapq
import sys
sys.stdin = open('../../a.txt', 'r')

def prim(i):
    global ans
    queue = []
    visit = [0] * (V + 1)
    heapq.heappush(queue, (0, i))

    while queue:
        cnt, i = heapq.heappop(queue)

        if visit[i]:
            continue

        ans += cnt
        visit[i] = 1

        for j in range(V+1):
            if graph[i][j] != 0 and visit[j] == 0:
                heapq.heappush(queue, (graph[i][j], j))


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    ans = 0
    prim(0)
    print(f"#{tc} {ans}")