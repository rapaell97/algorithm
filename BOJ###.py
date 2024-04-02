def find():
    blind = 0
    for i in range(N):
        for k in range(M):
            if lst[i][k] == 0:
                blind += 1

    return blind


def dfs(n):
    global ans

    if n == cnt:
        ans = min(ans, find())
        return

    i, k = cctv[n]
    direct = lst[i][k]
    for j in range(len(dic[direct])):
        origin_i, origin_k = i, k
        for p, q in dic[direct][j]:
            ni, nk = i + p, k + q
            # 각도 설정 끝났고 각도마다 출발해야댐


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
wall = []
for i in range(N):
    for k in range(M):
        if lst[i][k] != 0 or lst[i][k] != 6:
            cctv.append((i, k))
        elif lst[i][k] == 6:
            wall.append((i, k))

cnt = len(cctv)
ans = 21e8
dfs(0)
