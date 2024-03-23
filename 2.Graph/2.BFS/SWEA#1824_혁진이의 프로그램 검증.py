from collections import deque

move_1 = ['^', '>', 'v', '<']
move_2 = ['_', '|']
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

def bfs(i, k, c, m, d):
    queue = deque()
    queue.append((i, k, c, m, d))

    while queue:
        i, k, c, m, d = queue.popleft()

        if V[i][k][d][m]:
            continue

        V[i][k][d][m] = 1

        if c == '@':
            print(f"#{tc} YES")
            return

        if c in move_1:
            temp = move_1.index(c)
            ni = i + di[temp]
            nk = k + dk[temp]

            if 0 <= ni < R and 0 <= nk < C and V[ni][nk][temp][m] == 0:
                queue.append((ni, nk, lst[ni][nk], m, temp))

            elif ni < 0 and V[R - 1][nk][temp][m] == 0:
                queue.append((R - 1, nk, lst[R - 1][nk], m, temp))

            elif ni >= R and V[0][nk][temp][m] == 0:
                queue.append((0, nk, lst[0][nk], m, temp))

            elif nk < 0 and V[ni][C - 1][temp][m] == 0:
                queue.append((ni, C - 1, lst[ni][C - 1], m, temp))

            elif nk >= C and V[ni][0][temp][m] == 0:
                queue.append((ni, 0, lst[ni][0], m, temp))

        if c == '?':
            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0 <= ni < R and 0 <= nk < C and V[ni][nk][j][m] == 0:
                    queue.append((ni, nk, lst[ni][nk], m, j))

                elif ni < 0 and V[R - 1][nk][j][m] == 0:
                    queue.append((R - 1, nk, lst[R - 1][nk], m, j))

                elif ni >= R and V[0][nk][j][m] == 0:
                    queue.append((0, nk, lst[0][nk], m, j))

                elif nk < 0 and V[ni][C - 1][j][m] == 0:
                    queue.append((ni, C - 1, lst[ni][C - 1], m, j))

                elif nk >= C and V[ni][0][j][m] == 0:
                    queue.append((ni, 0, lst[ni][0], m, j))

        if c in move_2:
            if c == '_':
                if m == 0:
                    if k + 1 >= C and V[i][0][1][m] == 0:
                        queue.append((i, 0, lst[i][0], m, 1))
                    elif k + 1 < C and V[i][k + 1][1][m] == 0:
                        queue.append((i, k + 1, lst[i][k + 1], m, 1))

                else:
                    if k - 1 < 0 and V[i][C - 1][3][m] == 0:
                        queue.append((i, C - 1, lst[i][C - 1], m, 3))
                    elif k - 1 >= 0 and V[i][k - 1][3][m] == 0:
                        queue.append((i, k - 1, lst[i][k - 1], m, 3))

            else:
                if m == 0:
                    if i + 1 >= R and V[0][k][2][m] == 0:
                        queue.append((0, k, lst[0][k], m, 2))
                    elif i + 1 < R and V[i + 1][k][2][m] == 0:
                        queue.append((i + 1, k, lst[i + 1][k], m, 2))

                else:
                    if i - 1 < 0 and V[R - 1][k][0][m] == 0:
                        queue.append((R - 1, k, lst[R - 1][k], m, 0))
                    elif i - 1 >= 0 and V[i - 1][k][0][m] == 0:
                        queue.append((i - 1, k, lst[i - 1][k], m, 0))
        if c == '.':
            ni = i + di[d]
            nk = k + dk[d]

            if 0 <= ni < R and 0 <= nk < C and V[ni][nk][d][m] == 0:
                queue.append((ni, nk, lst[ni][nk], m, d))

            elif ni < 0 and V[R - 1][nk][d][m] == 0:
                queue.append((R - 1, nk, lst[R - 1][nk], m, d))

            elif ni >= R and V[0][nk][d][m] == 0:
                queue.append((0, nk, lst[0][nk], m, d))

            elif nk < 0 and V[ni][C - 1][d][m] == 0:
                queue.append((ni, C - 1, lst[ni][C - 1], m, d))

            elif nk >= C and V[ni][0][d][m] == 0:
                queue.append((ni, 0, lst[ni][0], m, d))

        if c.isdecimal():
            m = int(c)

            ni = i + di[d]
            nk = k + dk[d]

            if 0 <= ni < R and 0 <= nk < C and V[ni][nk][d][m] == 0:
                queue.append((ni, nk, lst[ni][nk], m, d))

            elif ni < 0 and V[R - 1][nk][d][m] == 0:
                queue.append((R - 1, nk, lst[R - 1][nk], m, d))

            elif ni >= R and V[0][nk][d][m] == 0:
                queue.append((0, nk, lst[0][nk], m, d))

            elif nk < 0 and V[ni][C - 1][d][m] == 0:
                queue.append((ni, C - 1, lst[ni][C - 1], m, d))

            elif nk >= C and V[ni][0][d][m] == 0:
                queue.append((ni, 0, lst[ni][0], m, d))

        if c == '+':
            if m == 15:
                m = 0
            else:
                m += 1

            ni = i + di[d]
            nk = k + dk[d]

            if 0 <= ni < R and 0 <= nk < C and V[ni][nk][d][m] == 0:
                queue.append((ni, nk, lst[ni][nk], m, d))

            elif ni < 0 and V[R - 1][nk][d][m] == 0:
                queue.append((R - 1, nk, lst[R - 1][nk], m, d))

            elif ni >= R and V[0][nk][d][m] == 0:
                queue.append((0, nk, lst[0][nk], m, d))

            elif nk < 0 and V[ni][C - 1][d][m] == 0:
                queue.append((ni, C - 1, lst[ni][C - 1], m, d))

            elif nk >= C and V[ni][0][d][m] == 0:
                queue.append((ni, 0, lst[ni][0], m, d))

        if c == '-':
            if m == 0:
                m = 15
            else:
                m -= 1

            ni = i + di[d]
            nk = k + dk[d]

            if 0 <= ni < R and 0 <= nk < C and V[ni][nk][d][m] == 0:
                queue.append((ni, nk, lst[ni][nk], m, d))

            elif ni < 0 and V[R - 1][nk][d][m] == 0:
                queue.append((R - 1, nk, lst[R - 1][nk], m, d))

            elif ni >= R and V[0][nk][d][m] == 0:
                queue.append((0, nk, lst[0][nk], m, d))

            elif nk < 0 and V[ni][C - 1][d][m] == 0:
                queue.append((ni, C - 1, lst[ni][C - 1], m, d))

            elif nk >= C and V[ni][0][d][m] == 0:
                queue.append((ni, 0, lst[ni][0], m, d))

        if c == '@':
            queue.append((i, k, '@', m, d))

    else:
        print(f"#{tc} NO")
        return


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    V = [[[[0] * 16 for _ in range(4)] for _ in range(C)] for _ in range(R)]
    lst = [list(input()) for _ in range(R)]

    flag = False
    for i in lst:
        for k in i:
            if k == '@':
                flag = True

    if flag:
        bfs(0, 0, lst[0][0], 0, 1)
    else:
        print(f"#{tc} NO")