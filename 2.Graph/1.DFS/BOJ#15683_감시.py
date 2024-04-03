def find():
    blind = 0
    for i in range(N):
        for k in range(M):
            if lst[i][k] == 0:
                blind += 1
    return blind


def back(arr):
    for i, k, o in arr:
        lst[i][k] = o


def dfs(n):
    global ans

    if n == cnt:
        ans = min(ans, find())
        return

    i, k, c_num = cctv[n]

    for j in range(len(dic[c_num])):
        temp = []
        for l in range(len(dic[c_num][j])):
            temp_i, temp_k = i, k
            p, q = dic[c_num][j][l]
            while True:
                temp_i = temp_i + p
                temp_k = temp_k + q

                if 0 <= temp_i < N and 0 <= temp_k < M and lst[temp_i][temp_k] != 6:
                    temp.append((temp_i, temp_k, lst[temp_i][temp_k]))
                    lst[temp_i][temp_k] = '#'
                else:
                    break

        dfs(n + 1)
        back(temp)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dic = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)]],
    5: [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
}

cctv = []
for i in range(N):
    for k in range(M):
        if 1 <= lst[i][k] < 6:
            cctv.append((i, k, lst[i][k]))

cnt = len(cctv)
ans = 21e8
dfs(0)

print(ans)
