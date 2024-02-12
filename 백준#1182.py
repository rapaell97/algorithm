def part_sum(i,temp,cnt):
    global ans
    if i == N:
        if temp == S and cnt > 0:
            ans += 1
        return
    part_sum(i+1,temp+lst[i],cnt+1)
    part_sum(i+1,temp,cnt)

N , S = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0
part_sum(0,0,0)
print(ans)