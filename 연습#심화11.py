from collections import deque
def bfs(s_i,s_k,e_i,e_k,cnt,check):
    queue = deque()
    queue.append((s_i,s_k,cnt))
    visit = [[0 for _ in range(N)]for _ in range(N)]

    while queue:
        i,k,cnt = queue.popleft()
        if i == e_i and k == e_k:
            return cnt
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if check == 0:
                if 0<= ni <N and 0<= nk <N and (fire_map[ni][nk] == '_' or fire_map[ni][nk] == 'A') and visit[ni][nk] == 0:
                    visit[ni][nk] = 1
                    queue.append((ni,nk,cnt+1))
            else:
                if 0<= ni <N and 0<= nk <N and (fire_map[ni][nk] == '_' or fire_map[ni][nk] == '$') and visit[ni][nk] == 0:
                    visit[ni][nk] = 1
                    queue.append((ni,nk,cnt+1))

N = int(input())
fire_map = [list(input()) for _ in range(N)]
min_i,min_k = map(int,input().split())
di = [-1,0,1,0]
dk = [0,1,0,-1]

sohwa = list()
fire_i, fire_k = 0, 0
for i in range(len(fire_map)):
    for k in range(len(fire_map[i])):
        if fire_map[i][k] == 'A':
            sohwa.append([i,k])
        if fire_map[i][k] == '$':
            fire_i = i
            fire_k = k

tosohwa = list()
for i in range(len(sohwa)):
    tosohwa.append(bfs(sohwa[i][0],sohwa[i][1],min_i,min_k,0,0))

ans_lst = list()
for i in range(len(sohwa)):
    ans_lst.append(tosohwa[i] + bfs(sohwa[i][0],sohwa[i][1],fire_i,fire_k,0,1))

print(min(ans_lst))