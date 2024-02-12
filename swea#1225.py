from collections import deque
for tc in range(1,11):
    T = int(input())
    queue = deque(map(int,input().split()))
    check = True
    while True:
        for i in range(1,6):
            temp = queue.popleft()
            if temp - i <= 0:
                queue.append(0)
                check = False
                break

            else:
                queue.append(temp-i)
        if not check:
            break

    print(f"#{tc}",*queue)