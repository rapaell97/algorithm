# 인덱스로 접근해서 point로 지울 위치를 지정해준 다음 yose에 추가하고 lst에서 지우는 식으로 하려다가
# k보다 작은 경우를 해결하지 못함

n,k = list(map(int,input().split()))
lst = list()
yose = list()

for i in range(1,n+1):
    lst.append(i)

point = k-1
while len(lst)>0:
    if len(lst)<point:
        while point<=len(lst)-1:
            point=(point%len(lst)-1)+(k-1)
        yose.append(lst[point])
        lst.remove(lst[point])


    else:
        if point>=len(lst)-1:
            point%=len(lst)
            yose.append(lst[point])
            lst.remove(lst[point])
            point+=k-1
        else:
            yose.append(lst[point])
            lst.remove(lst[point])
            point+=k-1
    if len(lst) == 0:
        break

yose_ch=str(yose).replace('[','<').replace(']','>')
print(yose_ch)

