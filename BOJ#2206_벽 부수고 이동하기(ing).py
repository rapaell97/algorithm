from collections import deque
import sys
sys.stdin = open ('my_input.txt', 'r')
input = sys.stdin.readline

def bfs(i, k, chance):
    global ans
    temp = 1
    visit = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((i, k, chance))
    visit[i][k] = 1
    while queue:

        print('#########################')
        print('temp : ',temp)
        for o in visit:
            for u in o:
                print(u,end=' ')
            print()

        for _ in range(len(queue)):
            i, k, chance = queue.popleft()

            if i == N - 1 and k == M - 1:
                if temp < ans:
                    ans = temp
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0:
                    if lst[ni][nk] == '0':
                        visit[ni][nk] = 1
                        queue.append((ni, nk, chance))

                    if chance == 1 and lst[ni][nk] == '1':
                        visit[ni][nk] = 1
                        queue.append((ni, nk, chance - 1))
        temp += 1

    else:
        ans = -1
        return

N , M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = 21e8
bfs(0, 0, 1)
print(ans)




