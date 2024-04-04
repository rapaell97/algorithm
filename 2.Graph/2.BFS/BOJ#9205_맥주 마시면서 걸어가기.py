from collections import deque


def bfs(i, k):
    queue = deque()
    queue.append((i, k))
    visit = [0] * N

    while queue:
        i, k = queue.popleft()

        if abs(end_i - i) + abs(end_k - k) <= 1000:
            return 'happy'

        for j in range(N):
            if visit[j] == 0:
                ni, nk = shop_lst[j]
                if abs(ni - i) + abs(nk - k) <= 1000:
                    visit[j] = 1
                    queue.append((ni, nk))
    else:
        return 'sad'


T = int(input())
for _ in range(T):
    N = int(input())
    start_i, start_k = map(int, input().split())

    shop_lst = []
    for i in range(N):
        a, b = map(int, input().split())
        shop_lst.append((a, b))

    end_i, end_k = map(int, input().split())

    print(bfs(start_i, start_k))
