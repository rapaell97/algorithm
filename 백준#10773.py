from collections import deque
test = int(input())
lst = [int(input()) for _ in range(test)]
queue = deque(lst)
ans_lst = list()

while len(queue) > 0:
    if queue[0] != 0:
        ans_lst.append(queue.popleft())
    else:
        queue.popleft()
        ans_lst.pop()

print(sum(ans_lst))

