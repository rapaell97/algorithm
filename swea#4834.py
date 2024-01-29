test = int(input())
for u in range(test):
    num = int(input())
    nums = list(input())

    int_nums = list()
    for i in range(num):
        int_nums.append(int(nums[i]))

    cnt_lst = [-1 for _ in range(10)]

    for i in int_nums:
        cnt_lst[i]+=1

    m = max(cnt_lst)

    if cnt_lst.count(m)>=2:
        same=list()
        for k in range(len(cnt_lst)):
            if cnt_lst[k] == m :
                same.append(k)
        print(f"#{u+1} {max(same)} {int_nums.count(max(same))}")
    else:
        print(f"#{u+1} {cnt_lst.index(m)} {int_nums.count(cnt_lst.index(m))}")

