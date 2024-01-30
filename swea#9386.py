test = int(input())
for u in range(test):
    num = int(input())
    lst = input()
    max_cnt = 0
    cnt = 0
    for i in lst:
        if i == '1':
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0

    print(f"#{u+1} {max_cnt}")