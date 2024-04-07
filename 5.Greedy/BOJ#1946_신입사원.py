import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    lst = []

    for _ in range(N):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst.sort()

    cnt = 1
    temp = lst[0][1]
    for i in range(1, N):
        t = lst[i][1]
        if t < temp:
            cnt += 1
            temp = t

    print(cnt)


