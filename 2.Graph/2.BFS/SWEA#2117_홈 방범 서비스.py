from collections import deque
import sys
sys.stdin = open('../../a.txt', 'r')


def bfs(i, j):
    visit = [[0] * N for _ in range(N)]
    global cnt

    if city[i][j] == 1:
        plus = M
        visit[i][j] = 1
        cnt += 1
    else:
        plus = 0
        visit[i][j] = 1

    K = 1
    queue = deque()
    queue.append((i, j))

    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()

            for l in range(4):
                ni = i + di[l]
                nj = j + dj[l]

                if 0<= ni <N and 0<= nj <N and visit[ni][nj] == 0:
                    visit[ni][nj] = 1
                    queue.append((ni, nj))

                    if city[ni][nj] == 1:
                        plus += M

        K += 1
        temp = K ** 2 + (K - 1) ** 2

        if plus >= temp:
            cnt = plus // M


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            bfs(i, j)
            ans = max(ans, cnt)

    print(f"#{tc} {ans}")
