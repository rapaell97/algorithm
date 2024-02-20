T = int(input())
for tc in range(1,T+1):
    N = int(input())

    di = [-1,-1,0,1,1,1,0,-1]
    dk = [0,1,1,1,0,-1,-1,-1]
    lst = [list(input()) for _ in range(N)]
    check = False
    for i in range(N):
        for k in range(N):
            if lst[i][k] == 'o':

                for j in range(8):
                    ni = i + di[j]
                    nk = k + dk[j]

                    if 0<= ni <N and 0<= nk <N and lst[ni][nk] == 'o':
                        temp_i = ni
                        temp_k = nk
                        temp = 0
                        for u in range(3):
                            temp_i = temp_i + di[j]
                            temp_k = temp_k + dk[j]
                            if 0<= temp_i <N and 0<= temp_k <N and lst[temp_i][temp_k] == 'o':
                                temp += 1
                            else:
                                break
                        if temp >= 3:
                            check = True
                            break
                if check:
                    break
                else:
                    lst[i][k] = '.'
        if check:
            break

    if check:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
