for tc in range(1,11):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for k in range(N):
        check = 0
        for i in range(N):
            if table[i][k] == 1:
                check = 1
            if table[i][k] == 2:
                if check:
                    ans += 1
                    check = 0

    print(f"#{tc} {ans}")