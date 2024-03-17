import sys
sys.stdin = open ('../my_input.txt', 'r')

def dfs(x):
    visit[x] = 1

    for j in graph[x]:
        if visit[j] == 0:
            dfs(j)

for tc in range(1 , 11):
    graph = [[] for _ in range(100)]
    visit = [0] * 100
    T , V = map(int, input().split())

    lst = list(map(int, input().split()))

    for i in range(0, len(lst) - 1, 2):
        graph[lst[i]].append(lst[i + 1])

    dfs(0)

    if visit[99] == 1:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")

