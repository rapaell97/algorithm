from collections import deque
def bfs(n, time):
    queue = deque()
    queue.append((n, time))
    while queue:
        i, time = queue.popleft()
        if i == K:
            ans_lst.append(time)
            return time
        for ni in (i - 1, i + 1, 2 * i):
            if ni == K:
                return time + 1
            elif 0 <= ni < ans and visit[ni] == 0:
                visit[ni] = 1
                queue.append((ni, time + 1))

N, K = map(int, input().split())
ans = 100000
visit = [0 for _ in range(ans + 1)]
ans_lst = list()
print(bfs(N, 0))
print(ans_lst)
