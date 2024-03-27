import heapq

def bfs(n, time):
    global ans
    queue = []
    heapq.heappush(queue, (time, n))
    V[n] = 1

    while queue:
        time, n = heapq.heappop(queue)

        if n == K:
            ans = time
            return

        temp = n * 2
        if temp < 100001 and V[temp] == 0:
            V[temp] = 1
            heapq.heappush(queue, (time, temp))

        for j in range(2):
            ni = n + di[j]
            if 0 <= ni < 100001 and V[ni] == 0:
                V[ni] = 1
                heapq.heappush(queue, (time + 1, ni))

di = [-1, 1]
N, K = map(int, input().split())
V = [0] * 100001

ans = 0
bfs(N, 0)
print(ans)
