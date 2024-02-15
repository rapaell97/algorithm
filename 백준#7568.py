test = int(input())
info_list=list()

for i in range(test):
    w,h=list(map(int,input().split()))
    info_list.append((w,h))

for k in info_list:
    cnt=1
    for j in info_list:
        if k[0]<j[0] and k[1]<j[1]:
            cnt+=1
    print(cnt,end=' ')
