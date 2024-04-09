import heapq

N = int(input())
mx_queue = []
mn_queue = []
ans = []
for i in range(N):
    num = int(input())

    if i == 0:
        mid = num

    else:
        if num <= mid:
            heapq.heappush(mx_queue, mid)
            heapq.heappush(mn_queue, -num)
            mid = -heapq.heappop(mn_queue)
        else:
            heapq.heappush(mx_queue, num)

        if len(mx_queue) - len(mn_queue) == 2:
            heapq.heappush(mn_queue, -mid)
            mid = heapq.heappop(mx_queue)

        elif len(mn_queue) - len(mx_queue) == 2:
            heapq.heappush(mx_queue, mid)
            mid = -heapq.heappop(mn_queue)

    print(mid)
