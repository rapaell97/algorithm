H, W = map(int, input().split())
lst = list(map(int, input().split()))

arr = [[0] * W for _ in range(H)]
for i in range(W):
    for j in range(lst[i]):
        arr[j][i] = 1

ans = 0
dj = [-1, 1]

for j in range(W):
    for i in range(H):
        if arr[i][j] == 0:
            left = False
            right = False

            oj = j
            while True:
                oj += dj[0]
                if oj == -1:
                    break
                if arr[i][oj] == 1:
                    left = True
                    break
            if left:
                oj = j
                while True:
                    oj += dj[1]
                    if oj == W:
                        break
                    if arr[i][oj] == 1:
                        right = True
                        break

            if left and right:
                ans += 1

print(ans)
