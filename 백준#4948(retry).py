lst = [True for _ in range(123456*2+1)]
for i in range(2,int((123456*2)**0.5)+1):
    if lst[i] == True:
        for j in range(2*i,len(lst),i):
            lst[j] = False
lst[0],lst[1] = False,False
while True:
    num = int(input())
    if num == 0:
         break
    else:
        print(lst[num+1:2*num+1].count(True))
