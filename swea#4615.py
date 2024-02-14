def change(p, q, color):
    lst[p][q] = color
    for j in range(8):
        np = p + dp[j]
        nq = q + dq[j]
        if 1 <= np < N + 1 and 1 <= nq < N + 1 and lst[np][nq] != color and lst[np][nq] != 0:
            m = np
            n = nq
            cnt = 0
            m_lst = list()
            n_lst = list()
            while True:
                cnt += 1
                m_lst.append(m)
                n_lst.append(n)
                m += dp[j]
                n += dq[j]
                if m < 1 or m >= N + 1 or n < 1 or n >= N + 1 or lst[m][n] == 0:
                    break
                if lst[m][n] == color:
                    for c in range(cnt):
                        a = m_lst[c]
                        b = n_lst[c]
                        lst[a][b] = color
                    break

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    dp = [-1, 1, 0, 0, -1, -1, 1, 1]
    dq = [0, 0, -1, 1, -1, 1, -1, 1]

    lst[N // 2][N // 2] = 2
    lst[N // 2 + 1][N // 2 + 1] = 2
    lst[N // 2 + 1][N // 2] = 1
    lst[N // 2][N // 2 + 1] = 1

    for i in range(M):
        q, p, color = map(int, input().split())
        change(p, q, color)

    black = 0
    white = 0
    for u in lst:
        for o in u:
            if o == 1:
                black+=1
            if o == 2:
                white+=1

    print(f"#{tc} {black} {white}")
