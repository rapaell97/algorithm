import sys
sys.stdin = open('../a.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(input())
    ans_lst = []

    point = N // 4
    turn = 0

    while turn < 30:

        for i in range(0, N, point):
            temp = str(''.join(lst[i : i + point]))
            temp = int(temp, 16)

            if temp not in ans_lst:
                ans_lst.append(temp)

        lst.insert(0, lst.pop())
        turn += 1

    ans_lst.sort(reverse=True)

    print(f"#{tc} {ans_lst[M - 1]}")
