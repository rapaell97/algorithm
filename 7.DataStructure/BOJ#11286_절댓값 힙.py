import sys
import heapq
sys.stdin = open('../a.txt', 'r')

input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(queue) == 0:
            print(0)
        else:
            x, y = heapq.heappop(queue)
            if y == -1:
                print(-x)
            else:
                print(x)

    else:
        if num < 0:
            heapq.heappush(queue, (abs(num), -1))
        else:
            heapq.heappush(queue, (abs(num), 1))