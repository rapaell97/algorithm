def dfs(i,k):
    visit[i][k] = 1
    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if visit[ni][nk] == 0 and 0<= ni <16 and 0<= nk <16 and graph[ni][nk] != 1:
            dfs(ni,nk)

for u in range(10):
    T = int(input())
    graph = [list(map(int,input())) for _ in range(16)]
    visit = [[0 for _ in range(16)] for _ in range(16)]
    di = [-1,0,1,0]
    dk = [0,1,0,-1]
    start_i,start_k,end_i,end_k = 0,0,0,0
    for i in range(len(graph)):
        for k in range(len(graph[i])):
            if graph[i][k] == 2:
                start_i = i
                start_k = k
            if graph[i][k] == 3:
                end_i = i
                end_k = k

    dfs(start_i,start_k)
    if visit[end_i][end_k] == 1:
        print(f"#{T} {1}")
    else:
        print(f"#{T} {0}")