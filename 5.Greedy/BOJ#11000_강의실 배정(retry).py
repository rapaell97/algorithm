import heapq
import sys
sys.stdin = open('../a.txt', 'r')

N = int(input())
queue = []
end_time = []

for i in range(N):
    s, e = map(int, input().split())
    queue.append([s, e])

queue.sort()
heapq.heappush(end_time, queue[0][1])

for i in range(1, N):
    if queue[i][0] < end_time[0]:
        heapq.heappush(end_time,queue[i][1])

    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time,queue[i][1])

print(len(end_time))
