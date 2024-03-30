from collections import deque

def bfs(i, k):
    global check
    queue = deque()
    queue.append((i, k))
    V[i][k] = 1

    while queue:
        i, k = queue.popleft()
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0 <= ni < 12 and 0 <= nk < 6 and V[ni][nk] == 0 and lst[ni][nk] == target:
                queue.append((ni, nk))
                temp.append((ni, nk))
                V[ni][nk] = 1

def down():
    for k in range(6):
        for i in range(10, -1, -1):
            if lst[i][k] != '.' and lst[i+1][k] == '.':
                c = lst[i][k]

                for j in range(i+1, 12):
                    if lst[j][k] != '.':
                        lst[j-1][k] = c
                        lst[i][k] = '.'
                        break

                    elif j == 11:
                        lst[j][k] = c
                        lst[i][k] = '.'


lst = [list(input()) for _ in range(12)]
colors = ['R', 'G', 'B', 'P', 'Y']
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = 0
while True:
    check = 0
    dic = {'R': [], 'G': [], 'B': [], 'P': [], 'Y': []}
    V = [[0] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for k in range(6):
            if lst[i][k] != '.' and V[i][k] == 0:
                temp = []
                target = lst[i][k]
                temp.append((i, k))
                bfs(i, k)

                if len(temp) >= 4:
                    dic[target].append(temp)
                    check = 1

    for color in colors:
        if len(dic[color]) != 0:
            for l in range(len(dic[color])):
                for p, q in dic[color][l]:
                    lst[p][q] = '.'

    down()
    for color in colors:
        dic[color].clear()

    if check:
        ans += 1
    else:
        break

print(ans)