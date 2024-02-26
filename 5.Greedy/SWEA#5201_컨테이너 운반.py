import sys
sys.stdin = open ('../my_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    T = list(map(int, input().split()))

    C.sort(reverse=True)
    T.sort(reverse=True)

    ans = 0
    i = 0

    for j in C:
        if j <= T[i]:
            ans += j
            i += 1

        if i == M:
            break

    print(f"#{tc} {ans}")







