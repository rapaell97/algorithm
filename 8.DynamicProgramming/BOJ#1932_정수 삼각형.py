N = int(input())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

if N == 1:
    print(*lst[0])
    exit()

d = [[] for _ in range(N)]
d[0] = lst[0]
d[1].append(d[0][0] + lst[1][0])
d[1].append(d[0][0] + lst[1][1])

for i in range(2, N):
    d[i].append(d[i-1][0]+lst[i][0])
    for j in range(1, i):
        temp = max(d[i-1][j-1]+lst[i][j], d[i-1][j]+lst[i][j])
        d[i].append(temp)
    d[i].append(d[i - 1][i-1] + lst[i][i])

print(max(d[N-1]))