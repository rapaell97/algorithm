import heapq

def prim(n):
    global ans
    queue = []
    heapq.heappush(queue, (0, n))

    while queue:
        dist, n = heapq.heappop(queue)
        if V[n]:
            continue
        V[n] = 1
        ans += dist

        for j in range(1, N + 1):
            if V[j] == 0:
                temp = (X[n] - X[j]) ** 2 + (Y[n] - Y[j]) ** 2
                heapq.heappush(queue, (temp, j))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    X = [0] + list(map(int, input().split()))
    Y = [0] + list(map(int, input().split()))
    E = float(input())

    V = [0] * (N + 1)

    ans = 0
    prim(1)

    print(round(ans * E))
