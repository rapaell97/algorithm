n,k = map(int,input().split())
lst = [True for _ in range(n+1)]
check = False
lst[0]=False
lst[1]=False
cnt = 0
ans = 0

for i in range(2,n):
    if lst[i] == True:
        for j in range(i,n+1,i):
            if cnt == k:
                check = True
                break
            elif lst[j] == True:
                lst[j] = False
                cnt += 1
                ans = j
    if check:
        break
print(ans)