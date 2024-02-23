import sys
sys.stdin = open ('my_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    parm = [list(map(int,input())) for _ in range(N)]
    mid = N // 2

    ans = 0
    for i in range(N):
        ans += parm[i][mid]

    left = (N - 1) // 2
    right = (N + 1) // 2

    idx = 1
    for k in range(left-1, -1, -1):
        for i in range(idx, N - idx):
            ans += parm[i][k]
        idx += 1

    idx = 1
    for k in range(right, N):
        for i in range(idx, N - idx):
            ans += parm[i][k]
        idx += 1

    print(f"#{tc} {ans}")