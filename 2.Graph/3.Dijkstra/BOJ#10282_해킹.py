import sys
input = sys.stdin.readline
import heapq


def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n))
    while queue:
        now_time, now = heapq.heappop(queue)

        if time[now] < now_time:
            continue

        for next, next_time in graph[now]:
            temp = time[now] + next_time
            if time[next] > temp:
                time[next] = temp
                heapq.heappush(queue, (temp, next))


T = int(input())
for tc in range(T):
    N, D, C = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(D):
        A, B, S = map(int, input().split())
        graph[B].append((A, S))

    INF = float('inf')
    time = [INF] * (N + 1)
    time[C] = 0

    dijkstra(C)

    ans_cnt, ans_time = 0, 0
    for i in time:
        if i != INF:
            ans_cnt += 1
            ans_time = max(ans_time, i)

    print(ans_cnt, ans_time)