n,k = map(int,input().split())
lst = [True for _ in range(n+1)]
check = False
lst[0]=False
lst[1]=False
cnt,ans = 0,0

for i in range(2,int(n**0.5)+1):
    if lst[i] == True:
        for j in range(i,n+1,i):
            if lst[j] == True:
                lst[j] = False
                cnt += 1
            if cnt == k:
                check = True
                ans = j
                break
    if check:
        break
print(ans)