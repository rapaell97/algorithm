test = int(input())
for u in range(test):
    num = int(input())
    lst = list(map(int, input().split()))

    new_lst = list()
    while True:
        max_num = 0
        min_num = 101
        max_index = 0
        min_index = 0

        for i in range(len(lst)):
            if lst[i] != 0:
                if lst[i] >= max_num:
                    max_num = lst[i]
                    max_index = i
        for k in range(len(lst)):
            if lst[k] != 0:
                if lst[k] <= min_num:
                    min_num = lst[k]
                    min_index = k

        new_lst.append(max_num)
        new_lst.append(min_num)

        for i in range(len(lst)):
            if i == max_index or i == min_index:
                lst[i] = 0
        if len(new_lst) == 10:
            break

    print(f"#{u+1}",*new_lst)


