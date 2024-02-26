from collections import deque
import sys
sys.stdin = open('../my_input.txt', 'r')
def bfs(i, k):
    visit = [[0] * N for _ in range(N)]
    visit[i][k] = 1
    queue = deque()
    queue.append((i, k))

    size = 2
    time = 0
    eat = 0

    while queue:
        if size == eat:
            eat = 0
            size += 1

        check = False
        for m in range(N):
            for n in range(N):
                if lst[m][n] != 0:
                    if lst[m][n] < size and visit[m][n] == 0:
                        check = True
                        break
            if check:
                break

        if not check:
            return time

        qsize = len(queue)

        for _ in range(qsize):
            i, k = queue.popleft()

            print('##########################################')
            print('size', size)
            print('eat', eat)
            print('time', time)
            print('list')
            for h in lst:
                for w in h:
                    print(w, end=' ')
                print()

            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            print('visit')
            for h in visit:
                for w in h:
                    print(w, end=' ')
                print()

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0 and lst[ni][nk] <= size:
                    if lst[ni][nk] != 0:
                        if lst[ni][nk] < size:
                            visit[ni][nk] = 1
                            lst[ni][nk] = 0
                            eat += 1
                            queue = deque()
                            queue.append((ni, nk))
                            visit = [[0] * N for _ in range(N)]
                            visit[ni][nk] = 1

                        if lst[ni][nk] == size:
                            visit[ni][nk] = 1
                            queue.append((ni, nk))

                    else:
                        visit[ni][nk] = 1
                        queue.append((ni, nk))
        time += 1

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, -1, 0, 1]

for i in range(N):
    for k in range(N):
        if lst[i][k] == 9:
            shark_i = i
            shark_k = k
            lst[i][k] = 0

ans = bfs(shark_i, shark_k)
print(ans)