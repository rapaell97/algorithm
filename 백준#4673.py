i=0
lst = list()
for i in range(1,10001):
    cnt = 0
    for j in range(i):
        str_num = str(j)
        sum=0
        for k in str_num:
            sum+=int(k)
        if j+sum == i:
            cnt+=1
    if cnt == 0:
        print(i)







