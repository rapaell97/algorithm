def dfs(s_i, s_k, chance, cnt):
    global max_cnt
    i = s_i
    k = s_k
    visit[i][k] = 1
    if cnt > max_cnt:
        max_cnt = max(cnt, max_cnt)

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0:
            if chance == 1 and lst[ni][nk] >= lst[i][k]:
                for gongsa in range(1, K + 1):
                    new = lst[ni][nk] - gongsa
                    if new < lst[i][k]:
                        dfs(ni, nk, chance - 1, cnt + 1)

                        # if i == 2 and k == 3:
                        #     for o in visit:
                        #         for u in o:
                        #             print(u, end='')
                        #         print()
                        #     print('#############################################')

                        visit[ni][nk] = 0
                        break
            else:
                if lst[ni][nk] < lst[i][k]:
                    dfs(ni, nk, chance, cnt + 1)

                    # if i == 2 and k == 3:
                    #     for o in visit:
                    #         for u in o:
                    #             print(u, end='')
                    #         print()
                    #     print('#############################################')

                    visit[ni][nk] = 0

T = int(input())
for tc in range(1,T+1):
    N , K = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)]for _ in range(N)]
    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]

    high = 0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] > high :
                high = lst[i][k]

    high_lst = list()
    low_lst = list()
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] == high:
                high_lst.append([i,k])

    max_cnt = 0
    print(high_lst)
    for i in range(len(high_lst)):
        visit = [[0 for _ in range(N)] for _ in range(N)]
        dfs(high_lst[i][0], high_lst[i][1],1, 1)

    print(f"#{tc} {max_cnt}")
