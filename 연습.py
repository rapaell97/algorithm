lst=[[0 for _ in range(3)]for _ in range(2)]
lst2=list(map(int,input().split()))

for i in range(len(lst)):
    for k in range(len(lst[i])):
        lst[i][k]=lst2.pop()

lst3=[0 for _ in range(6)]

cnt=0
for i in range(len(lst)):
    for k in range(len(lst[i])):
        lst3[cnt]=lst[i][k]
        cnt+=1

lst3[0],lst3[5]=lst3[5],lst3[0]

print(*lst3)