for u in range(1,11):
    test, case = map(int,input().split())
    tc = list(map(int,input().split()))
    graph = [[] for _ in range(100)]
    visit = [0 for _ in range(100)]
    for i in range(0,len(tc)-1,2):
        graph[tc[i]].append(tc[i+1])
    def dfs_stack(node):
        stack = [node]
        while stack:
            now = stack.pop()
            for i in graph[now]:
                if visit[i] == 0:
                    stack.append(i)
            visit[now] = 1
    dfs_stack(0)
    if visit[-1] == 1:
        print(f"#{u} 1")
    else:
        print(f"#{u} 0")
