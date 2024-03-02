N = int(input())
lst = [[0] * 30 for _ in range(30)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

for i in range(N):
    a, b = map(int, input().split())

    for p in range(b, b + 10):
        for q in range(a, a + 10):
            if lst[p][q] == 0:
                lst[p][q] = 1

ans = 0
for i in range(30):
    for k in range(30):
        if lst[i][k] == 1:
            temp = 0

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <101 and 0<= nk <101 and lst[ni][nk] == 0:
                    temp += 1

            if temp >= 2:
                ans += 2
            elif temp == 1:
                ans += 1

print(ans)






