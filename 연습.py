from collections import deque
import sys
input = sys.stdin.readline
def bfs(ei,ek,cnt):
    queue = deque()
    queue.append((goal_i,goal_k,cnt))
    while queue:
        i,k,cnt = queue.popleft()
        if i == ei and k == ek:
            return cnt
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0 and lst[ni][nk] != 0:
                visit[ni][nk] += 1
                queue.append((ni,nk,cnt+1))
    else:
        return -1

N , M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]

for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == 2:
            goal_i = i
            goal_k = k

di = [-1,0,1,0]
dk = [0,1,0,-1]

visit = [[0 for _ in range(M)] for _ in range(M)]
bfs()
for o in visit:
    for u in o:
        print(u,end=' ')
    print()

