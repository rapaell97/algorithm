test = int(input())
for u in range(test):
    range_num = int(input())
    range_lst = list()
    for i in range(range_num):
        a, b = list(map(int, input().split()))
        sub_lst = list()
        for k in range(a, b+1):
            sub_lst.append(k)
        range_lst.append(sub_lst)

    stop = int(input())
    stop_lst = list()
    for i in range(stop):
        a = int(input())
        stop_lst.append(a)

    result = [0 for _ in range(stop)]

    for i in range(stop):
        for k in range(len(range_lst)):
            if stop_lst[i] in range_lst[k]:
                result[i] += 1

    print(f"#{u+1}",*result)

