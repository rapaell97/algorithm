N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst2 = sorted(lst, key=lambda x: (x[0], x[1]), reverse=True)

i = 0
while i < N:
    if lst2[0][0]