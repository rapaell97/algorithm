from collections import deque


def bfs(n):
    global time
    queue = deque()
    queue.append(n)
    lst[n] = 2

    while queue:
        for _ in range(len(queue)):
            i = queue.popleft()

            if i == K:
                return

            for ni in (i - 1, i + 1, 2 * i):
                if 0 <= ni <= len(lst) and lst[ni] != 2:
                    lst[ni] = 2
                    queue.append(ni)

        time += 1


N, K = map(int, input().split())
lst = [0] * (100000 + 1)
lst[N], lst[K] = 1, 1

time = 0
bfs(N)
print(time)
