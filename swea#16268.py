test = int(input())
for u in range(test):
    n,m = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(n)]

    di=[0, -1, 0, 1, 0]
    dk=[0, 0, 1, 0, -1]

    sum_lst = list()
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            check = 0
            for r in range(5):
                ni = i + di[r]
                nk = k + dk[r]

                if 0 <= ni < n and 0 <= nk < m:
                    check += lst[ni][nk]
            sum_lst.append(check)
    print(f"#{u+1} {max(sum_lst)}")