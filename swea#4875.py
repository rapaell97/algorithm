def dfs(i,k):
    stack = [(i,k)]
    while stack:
        p,q = stack.pop()
        for j in range(4):
            np = p + di[j]
            nq = q + dk[j]
            if 0<= np <N and 0<= nq <N and visit[np][nq] == 0 and (lst[np][nq] == 0 or lst[np][nq] == 3):
                stack.append((np,nq))
                visit[np][nq] = 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    di = [-1,0,1,0]
    dk = [0,1,0,-1]
    s_i,s_k,e_i,e_k = 0,0,0,0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] == 2:
                s_i = i
                s_k = k
            if lst[i][k] == 3:
                e_i = i
                e_k = k
    dfs(s_i,s_k)
    if visit[e_i][e_k] == 1:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")

