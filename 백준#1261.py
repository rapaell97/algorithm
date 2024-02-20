def dfs(i,k,cnt):
    global min_cnt

    visit[i][k] = 1
    print(cnt)
    print(min_cnt)

    if i == N-1 and k == M-1:

        for o in visit:
            for u in o:
                print(u, end=' ')
            print()
        print('##########################################')
        return

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0:
            if lst[ni][nk] == '1':
                dfs(ni,nk,cnt+1)
                visit[ni][nk] = 0
            else:
                dfs(ni,nk,cnt)
                visit[ni][nk] = 0
    if cnt < min_cnt:
        min_cnt = cnt

M , N = map(int,input().split())
lst = [list(input()) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

min_cnt = N*M

dfs(0,0,0)
print(min_cnt)

