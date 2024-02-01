test = int(input())
for u in range(test):
    num = int(input())
    lst = list(map(int,input().split()))
    i = 0
    mx_cnt = 1
    cnt = 1
    while i < num-1:
        if lst[i] < lst[i+1]:
            cnt += 1
            mx_cnt = max(cnt,mx_cnt)

        else:
            cnt = 1

        i+=1

    print(f"#{u+1} {mx_cnt}")
