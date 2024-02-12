def bfs(i,k):
    stack = [(i,k)]
    while stack:
        p,q = stack.pop()
        for j in range(4):
            np = p + di[j]
            nq = q + dk[j]
            if visit[np][nq] == 0 and 0<= np <100 and 0<= nq <100 and graph[np][nq] != 1:
                stack.append((np,nq))
                visit[np][nq] = 1

for u in range(10):
    T = int(input())
    graph = [list(map(int,input())) for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]
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

    bfs(start_i,start_k)
    if visit[end_i][end_k] == 1:
        print(f"#{T} {1}")
    else:
        print(f"#{T} {0}")