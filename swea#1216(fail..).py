for _ in range(10):
    tc = int(input())
    lst = [list(input())for _ in range(100)]

    max_cnt = 0
    for i in range(100):
        for k in range(100):
            for j in range(k,100):
                temp = 0
                if lst[i][k] == lst[i][j]:
                    temp_lst = lst[i][k:j+1]
                    if temp_lst == temp_lst[::-1]:
                        temp = len(temp_lst)
                if temp>max_cnt:
                    max_cnt = temp

    for k in range(100):
        for i in range(100):
            for j in range(k,100):
                temp = 0
                if lst[i][k] == lst[j][k]:
                    temp_lst = list()
                    for r in range(i,j+1):
                        temp_lst.append(lst[r][k])
                    if temp_lst == temp_lst[::-1]:
                        temp = len(temp_lst)
                if temp>max_cnt:
                    max_cnt = temp
    print(f"#{tc} {max_cnt}")
