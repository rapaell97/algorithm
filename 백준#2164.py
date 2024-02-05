from collections import deque
num = int(input())
lst= [x for x in range(1, num+1)]
queue = deque(lst)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)
