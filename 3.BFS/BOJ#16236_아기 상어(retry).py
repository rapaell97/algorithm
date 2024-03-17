import sys
from collections import deque

sys.stdin = open('../a.txt', 'r')


def bfs(i, k):
    V = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((i, k))
    ans, time = 0, 0
    size = 2
    eat = 0
    fish = []
    while queue:
        if len(fish) != 0:
            V = [[0] * N for _ in range(N)]
            fish.sort(key=lambda x: (x[0], x[1]))
            queue.clear()
            queue.append((fish[0][0], fish[0][1]))
            lst[fish[0][0]][fish[0][1]] = 0
            ans = time
            fish.clear()
            eat += 1

        if eat == size:
            size += 1
            eat = 0

        for _ in range(len(queue)):
            i, k = queue.popleft()
            V[i][k] = 1

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0 <= ni < N and 0 <= nk < N and V[ni][nk] == 0 and lst[ni][nk] <= size:
                    if lst[ni][nk] == size or lst[ni][nk] == 0:
                        V[i][k] = 1
                        queue.append((ni, nk))

                    else:
                        V[i][k] = 1
                        fish.append([ni, nk])
                        queue.append((ni, nk))

        check = False
        for p in lst:
            for q in p:
                if q != 0 and q < size:
                    check = True
                    break

        if not check:
            print(time)
            return
        time += 1

    else:
        print(ans)
        return


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

for i in range(N):
    for k in range(N):
        if lst[i][k] == 9:
            s_i = i
            s_k = k
            lst[i][k] = 0

bfs(s_i, s_k)
