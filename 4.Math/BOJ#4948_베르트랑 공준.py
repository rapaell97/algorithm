import sys
sys.stdin = open('../a.txt', 'r')

while True:
    N = int(input())
    if N == 0:
        break
    M = 2*N
    lst = [True] * (M+1)
    lst[0], lst[1] = False, False

    for i in range(2, M+1):
        if lst[i]:
            for j in range(2*i, M+1, i):
                if lst[j]:
                    lst[j] = False

    cnt = 0
    for i in range(N+1, M+1):
        if lst[i]:
            cnt += 1

    print(cnt)


