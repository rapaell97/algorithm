import sys
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    mx_q = []
    mn_q = []

    K = int(input())
    check = [1] * K
    for i in range(K):
        com, num = input().split()

        if com == "I":
            heapq.heappush(mx_q, (-int(num), i))
            heapq.heappush(mn_q, (int(num), i))

        else:
            if len(mn_q) == 0:
                continue

            if num == '-1':
                while mn_q:
                    temp, idx = heapq.heappop(mn_q)
                    if check[idx] == 1:
                        check[idx] = 0
                        break

            else:
                while mx_q:
                    temp, idx = heapq.heappop(mx_q)
                    if check[idx] == 1:
                        check[idx] = 0
                        break
    flag1 = False
    ans_mn = 0
    while mn_q:
        temp_mn, temp_idx = heapq.heappop(mn_q)
        if check[temp_idx] == 1:
            flag1 = True
            ans_mn = temp_mn
            break

    flag2 = False
    ans_mx = 0
    while mx_q:
        temp_mx, temp_idx = heapq.heappop(mx_q)
        if check[temp_idx] == 1:
            flag2 = True
            ans_mx = -temp_mx
            break

    if flag1 and flag2:
        print(ans_mx, ans_mn)

    else:
        print("EMPTY")