def howmuch(arr,x):
    lst = [int(x) for x in arr]

    for i in range(int(x)):
        max_num = 0
        for j in range(i,len(lst)):
            if lst[j] >= max_num:
                max_num = lst[j]
                max_index = j

        for k in range(len(lst)):
            if k == max_index:
                lst[i],lst[k] = lst[k],lst[i]
                max_num = 0
    return lst

test = int(input())
for u in range(test):
    num,c = input().split()
    print(f"#{u+1}\n")
    print(*howmuch(num,c))
