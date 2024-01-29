for u in range(10):
    b_num = int(input())
    lst = [[0 for _ in range(256)] for _ in range(b_num)]
    h_lst = list(map(int,input().split()))

    for i in range(b_num):
        for k in range(h_lst[i]):
            lst[i][k]=1

    # for i in lst:
    #     for k in i:
    #         print(k,end='')
    #     print()

    cnt=0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] == 1:
                if lst[i-2][k] == 0 and lst[i-1][k] == 0 and lst[i+1][k] == 0 and lst[i+2][k] == 0:
                    cnt += 1


    print(f"#{u+1} {cnt}")



