import sys
sys.stdin = open('../my_input.txt', 'r')


def choice(n, start):
    global ans

    if n == point:
        temp_1 = path
        temp_2 = [t for t in lst if t not in temp_1]

        A = 0
        for p in range(point - 1):
            for q in range(p + 1, point):
                A += graph[temp_1[p]][temp_1[q]] + graph[temp_1[q]][temp_1[p]]

        B = 0
        for p in range(point - 1):
            for q in range(p + 1, point):
                B += graph[temp_2[p]][temp_2[q]] + graph[temp_2[q]][temp_2[p]]

        R = abs(A - B)

        if R < ans:
            ans = R

        return

    for j in range(start, N):
        if use[j] == 0:
            use[j] = 1
            path[n] = lst[j]
            choice(n + 1, j)
            use[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    point = N // 2

    lst = list(range(N))
    use = [0] * N
    path = [0] * point

    ans = 21e8
    choice(0, 0)
    print(f"#{tc} {ans}")
