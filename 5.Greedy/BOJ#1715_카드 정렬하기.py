import heapq
import sys
input = sys.stdin.readline

queue = []
N = int(input())
for _ in range(N):
    heapq.heappush(queue, int(input()))

ans = 0
while True:
    temp1 = heapq.heappop(queue)
    if len(queue) == 0:
        break
    temp2 = heapq.heappop(queue)
    temp3 = temp1 + temp2
    ans += temp3

    heapq.heappush(queue, temp3)

print(ans)
