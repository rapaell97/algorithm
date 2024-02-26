def dfs(node):
    visit[node] = 1
    for i in range(1, v+1):
        if visit[i] == 0 and lst[node][i] == 1:
            dfs(i)

tc = int(input())
for u in range(tc):
    v, e = map(int,input().split())
    visit = [0 for _ in range(v+1)]
    lst = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        start , end = map(int,input().split())
        lst[start][end] = 1

    s, g = map(int,input().split())
    dfs(s)

    if visit[g] == 1:
        print(f"#{u+1} 1")
    else:
        print(f"#{u+1} 0")

