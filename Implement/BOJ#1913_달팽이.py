N = int(input())
num = int(input())

lst = [[0] * N for _ in range(N)]
di = [1, 0, -1, 0]
dk = [0, 1, 0, -1]

i, k, d = 0, 0, 0
for t in range(N ** 2, 0, -1):
    lst[i][k] = t

    ni = i + di[d]
    nk = k + dk[d]

    if 0<= ni <N and 0<= nk <N and lst[ni][nk] == 0:
        i = ni
        k = nk
    else:
        d = (d + 1) % 4
        i = i + di[d]
        k = k + dk[d]

for i in range(N):
    for k in range(N):
        print(lst[i][k], end = ' ')

        if lst[i][k] == num:
            ans_i = i
            ans_k = k
    print()

print(ans_i + 1, ans_k + 1)