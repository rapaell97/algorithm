import sys
sys.setrecursionlimit(10**6)
def dfs_A(i,k):
    visit_A[i][k] = 1
    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0<= ni <N and 0<= nk <N and lst[i][k] == lst[ni][nk] and visit_A[ni][nk] == 0:
            dfs_A(ni,nk)

def dfs_B(i,k):
    visit_B[i][k] = 1
    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0<= ni <N and 0<= nk <N and visit_B[ni][nk] == 0:
            if lst[i][k] == 'R' or lst[i][k] == 'G':
                if lst[ni][nk] == 'R' or lst[ni][nk] == 'G':
                    dfs_B(ni,nk)
            else:
                if lst[i][k] == lst[ni][nk]:
                    dfs_B(ni,nk)

N = int(input())
lst = [list(input()) for _ in range(N)]
visit_A = [[0 for _ in range(N)] for _ in range(N)]
visit_B = [[0 for _ in range(N)] for _ in range(N)]
di = [-1,0,1,0]
dk = [0,1,0,-1]

cnt_A = 0
for i in range(len(lst)):
    for k in range(len(lst[i])):
        if visit_A[i][k] == 0:
            dfs_A(i,k)
            cnt_A += 1
cnt_B = 0
for i in range(len(lst)):
    for k in range(len(lst[i])):
        if visit_B[i][k] == 0:
            dfs_B(i,k)
            cnt_B += 1
print(cnt_A,cnt_B)

