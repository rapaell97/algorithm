import sys
sys.stdin = open('../a.txt', 'r')
input = sys.stdin.readline
import heapq
N = int(input())
queue = []

for _ in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(queue, a)

    else:
        if len(queue) == 0:
            print(0)
        else:
            print(heapq.heappop(queue))


