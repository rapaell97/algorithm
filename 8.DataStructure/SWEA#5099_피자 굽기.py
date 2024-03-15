from collections import deque
T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    lst = list(map(int,input().split()))
    queue = deque()
    for i in range(N):
        queue.append(i)
    k = N

    while True:
        temp_index = queue.popleft()
        lst[temp_index] //= 2
        if lst[temp_index] <= 1:
            if k < M:
                queue.append(k)
                k += 1
            else:
                if lst[temp_index] >= 2:
                    queue.append(temp_index)
        else:
            if lst[temp_index] >= 2:
                queue.append(temp_index)
        if len(queue) == 0:
            break

    print(f"#{tc} {temp_index+1}")
