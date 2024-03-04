import heapq

hq = []

for i in range(10, 0 , -1):
    heapq.heappush(hq, i)
    print(hq)

print(hq)