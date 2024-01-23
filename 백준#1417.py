num = int(input())
lst=list()
for i in range(num):
    a=int(input())
    lst.append(a)

cnt=0
while True:
    m = lst.index(max(lst))
    if lst[0]<lst[m]:
        lst[0]+=1
        lst[m]-=1
        cnt+=1

    if lst[0] == max(lst):
        break

if lst.count(max(lst)) != 1:
    cnt+=1
    print(cnt)
else:
    print(cnt)






