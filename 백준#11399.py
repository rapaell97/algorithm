num = int(input())
lst = list(map(int,input().split()))
lst.sort()
ans = 0
for i in range(len(lst)+1):
    ans+=sum(lst[0:i])
print(ans)