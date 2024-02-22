T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0, 0]]

    ans = 0
    for i in range(N):
        a, b = map(int, input().split())

        for j in lst:
            if a > j[0] and b < j[1]:
                ans += 1
            elif a < j[0] and b > j[1]:
                ans += 1

        lst.append([a, b])

    print(f"#{tc} {ans}")








