n, m = map(int,input().split())
lst = list(map(int,input().split()))

sum_lst = list()
for i in range(len(lst)-2):
    for k in range(i+1,len(lst)-1):
        for j in range(k+1,len(lst)):
            check = lst[i]+lst[k]+lst[j]
            if check <= m:
                sum_lst.append(check)

print(max(sum_lst))


