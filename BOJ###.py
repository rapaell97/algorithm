import sys

sys.stdin = open('a.txt', 'r')
import heapq


def bfs(n, time):
    global ans
    queue = []
    heapq.heappush(queue, (time, n))
    V[n] = 1

    while queue:
        time, n = heapq.heappop(queue)
        #
        # print('######################')
        # print('시간 :', time)
        # print('위치 :', n)

        if n == K:
            ans = time
            return

        for j in range(2):
            ni = n + di[j]
            if 0 <= ni <= (K * 2) and V[ni] == 0:
                V[ni] = 1
                heapq.heappush(queue, (time + 1, ni))
        if n != 0:
            temp = n
            while True:
                temp *= 2

                if temp > 2 * K:
                    break
                if V[temp] == 0:
                    V[temp] = 1
                    heapq.heappush(queue, (time, temp))


di = [-1, 1]
N, K = map(int, input().split())
V = [0] * 200001

ans = 0
bfs(N, 0)

print(ans)
