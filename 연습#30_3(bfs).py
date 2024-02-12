from collections import deque
def bfs(n):
    queue = deque([n])
    visit[n] = 1
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in range(6):
            if lst[now][i] == 1 and visit[i] == 0:
                visit[i] = 1
                queue.append(i)

lst =[[0,1,0,0,1,0],
      [0,0,1,0,0,1],
      [0,0,0,1,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]]
visit = [0 for _ in range(6)]
bfs(0)