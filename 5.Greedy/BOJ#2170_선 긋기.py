N = int(input())
lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    temp.sort()
    lst.append(temp)

lst.sort()

ans = lst[0][1] - lst[0][0]
end = lst[0][1]

i = 1
while i < N:
    if lst[i][1] > end:

        if lst[i][0] < end:
            ans += lst[i][1] - end

        else:
            ans += lst[i][1] - lst[i][0]

        end = lst[i][1]

    i += 1

print(ans)
