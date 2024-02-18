def dfs(i, k, chance, cnt):
    global max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
    visit[i][k] = 1
    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0:
            if lst[i][k] > lst[ni][nk]:
                dfs(ni,nk,chance,cnt+1)
            else:
                if chance == 1 and lst[i][k] > lst[ni][nk] - K:
                    temp = lst[ni][nk]
                    lst[ni][nk] = lst[i][k] - 1
                    dfs(ni,nk,0,cnt+1)
                    lst[ni][nk] = temp
    visit[i][k] = 0

T = int(input())
for tc in range(1,T+1):
    N , K = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)]for _ in range(N)]
    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]

    high = 0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] > high :
                high = lst[i][k]
    max_cnt = 0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] == high:
                dfs(i,k,1,1)

    print(f"#{tc} {max_cnt}")
