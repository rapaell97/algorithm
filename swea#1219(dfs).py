def dfs(node):
    visit[node] = 1
    for i in range(100):
        if visit[i] == 0 and graph[node][i] == 1:
            dfs(i)

for u in range(10):
    t, c = map(int, input().split())
    lst = list(map(int, input().split()))
    visit = [0 for _ in range(100)]
    graph = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(0, len(lst)-1, 2):
        graph[lst[i]][lst[i+1]] = 1

    dfs(0)
    if visit[99] == 1:
        print(f"#{u+1} 1")
    else:
        print(f"#{u+1} 0")
