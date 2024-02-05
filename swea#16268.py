def pang(arr,x,y):
    di = [0, -1, 0, 1, 0]
    dk = [0, 0, 1, 0, -1]

    sum_lst = list()
    for i in range(len(arr)):
        for k in range(len(arr[i])):
            check = 0
            for r in range(5):
                ni = i + di[r]
                nk = k + dk[r]

                if 0 <= ni < x and 0 <= nk < y:
                    check += lst[ni][nk]
            sum_lst.append(check)
    return max(sum_lst)

test = int(input())
for u in range(test):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{u+1} {pang(lst,n,m)}")
