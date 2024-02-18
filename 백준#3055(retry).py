from collections import deque
def flood(si,sk):
    for j in range(4):
        ni = si + di[j]
        nk = sk + dk[j]
        if 0<= ni <N and 0<= nk <M and (lst[ni][nk] == '.' or lst[ni][nk] == 'S'):
            lst[ni][nk] = '*'

def bfs(si,sk,cnt):
    queue = deque()
    queue.append((si,sk,cnt))
    while queue:
        water = list()
        for p in range(len(lst)):
            for q in range(len(lst[p])):
                if lst[p][q] == '*':
                    water.append([p, q])
        if len(water) != 0:
            for w in water:
                flood(w[0], w[1])
        for _ in range(len(queue)):
            i, k, cnt = queue.popleft()
            if i == vi_i and k == vi_k:
                return cnt
            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0 and (lst[ni][nk] == '.' or lst[ni][nk] == 'D' ):
                    visit[ni][nk] = 1
                    lst[ni][nk] = 'S'
                    queue.append((ni,nk,cnt+1))
    else:
        return 'KAKTUS'

N, M = map(int,input().split())
lst = [list(input()) for _ in range(N)]
visit = [[0 for _ in range(M)]for _ in range(N)]
di = [-1,0,1,0]
dk = [0,1,0,-1]

go_i,go_k,vi_i,vi_k = 0,0,0,0
for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == 'D':
            vi_i = i
            vi_k = k
        if lst[i][k] == 'S':
            go_i = i
            go_k = k

print(bfs(go_i,go_k,0))
