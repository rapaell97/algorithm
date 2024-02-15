from collections import deque
def bfs(s_i,s_k,e_i,e_k,cnt):
    queue = deque()
    queue.append((s_i,s_k,cnt))
    visit = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        i, k, cnt = queue.popleft()
        if i == e_i and k == e_k:
            return cnt
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni <N and 0<= nk <M and (lst[ni][nk] == '.' or lst[ni][nk] == 'D' or lst[ni][nk] == 'C' ) and visit[ni][nk] == 0 :
                visit[ni][nk] = 1
                queue.append((ni,nk,cnt+1))

N , M = map(int,input().split())
lst = [list(input().split()) for _ in range(N)]
sigol_i,sigol_k,dosi_i,dosi_k,c_i,c_k = 0,0,0,0,0,0
di = [-1,0,1,0]
dk = [0,1,0,-1]

for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == 'S':
            sigol_i = i
            sigol_k = k
        if lst[i][k] == 'D':
            dosi_i = i
            dosi_k = k
        if lst[i][k] == 'C':
            c_i = i
            c_k = k
print(bfs(sigol_i,sigol_k,c_i,c_k,0) + bfs(c_i,c_k,dosi_i,dosi_k,0))
