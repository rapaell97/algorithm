import sys

sys.stdin = open('a.txt', 'r')
import heapq


def prim(n):
    global price
    queue = []
    heapq.heappush(queue, (0, n))

    while queue:
        dist, n = heapq.heappop(queue)
        lst.append(dist)

        for j in range(1, N + 1):
            if V[j] == 0:
                temp = (X[n] - X[j]) ** 2 + (Y[n] - Y[j]) ** 2
                heapq.heappush(queue,(temp, j))
        V[n] = 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    X = [0] + list(map(int, input().split()))
    Y = [0] + list(map(int, input().split()))
    E = float(input())

    V = [0] * (N + 1)

    lst = []
    prim(1)

    ans = 0
    for i in range(N):
        ans += (E * (lst[i] ** 2))

    print(round(ans, 1))

