import sys
sys.stdin = open ('../my_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x: (x[1], x[0]))

    i = 0
    j = 1
    ans = 1

    while i < N - 1 and j < N:
        if lst[i][1] <= lst[j][0]:
            ans += 1
            i = j
            j += 1

        else:
            j += 1

    print(f"#{tc} {ans}")
