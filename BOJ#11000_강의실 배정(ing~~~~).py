import sys
sys.stdin = open('a.txt', 'r')
input = sys.stdin.readline
import heapq

N = int(input())
queue = []

for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(queue, (s, e))

cnt = 0
temp_end = []
for i in range(N):
    s, e = heapq.heappop(queue)

    check = False
    temp_idx = 0
    temp1 = 10**9
    for j in range(len(temp_end)):
        if e >= temp_end[j]:
            temp2 = e - temp_end[j]

            if temp2 > temp1:
                temp1 = temp2
                temp_idx = j
                check = True

    if check:
        temp_end.remove(temp_idx)
        temp_end.append(e)

    else:
        temp_end.append(e)
        cnt += 1

print(cnt - 1)
