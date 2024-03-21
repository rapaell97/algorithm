import sys
sys.stdin = open('../a.txt', 'r')

N, M = map(int, input().split())
arr = [[0] * (M + 1) for _ in range(N + 1)]
lst = [[0, 0]]

for _ in range(N):
    lst.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for k in range(1, M + 1):
        W = lst[i][0]
        V = lst[i][1]

        if k < W:
            arr[i][k] = arr[i - 1][k]
        else:
            arr[i][k] = max(V + arr[i - 1][k - W], arr[i - 1][k])

print(arr[N][M])