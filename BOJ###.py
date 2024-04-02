N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dic = {
    1: [[], [], [], []],
    2: [[], []],
    3: [],
    4: [],
    5: []
}

cctv = []
wall = []
for i in range(N):
    for k in range(M):
        if lst[i][k] != 0 or lst[i][k] != 6:
            cctv.append((i, k))
        elif lst[i][k] == 6:
            wall.append((i, k))
