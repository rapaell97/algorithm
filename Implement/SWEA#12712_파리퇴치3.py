T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]

    di_1 = [-1,0,1,0]
    dk_1 = [0,1,0,-1]
    di_2 = [-1,-1,1,1]
    dk_2 = [-1,1,1,-1]

    ans = 0
    for i in range(N):
        for k in range(N):
            temp_1 = lst[i][k]
            temp_2 = lst[i][k]

            for j in range(4):
                p_1 = i + di_1[j]
                q_1 = k + dk_1[j]
                p_2 = i + di_2[j]
                q_2 = k + dk_2[j]

                if 0 <= p_1 <N and 0 <= q_1 <N:
                    temp_1 += lst[p_1][q_1]
                    for l in range(M - 2):
                        p_1 = p_1 + di_1[j]
                        q_1 = q_1 + dk_1[j]
                        if 0 <= p_1 < N and 0 <= q_1 < N:
                            temp_1 += lst[p_1][q_1]

                if 0 <= p_2 < N and 0 <= q_2 < N:
                    temp_2 += lst[p_2][q_2]
                    for l in range(M - 2):
                        p_2 = p_2 + di_2[j]
                        q_2 = q_2 + dk_2[j]
                        if 0 <= p_2 < N and 0 <= q_2 < N:
                            temp_2 += lst[p_2][q_2]

            temp_result = max(temp_1,temp_2)
            if temp_result > ans:
                ans = temp_result

    print(f"#{tc} {ans}")
