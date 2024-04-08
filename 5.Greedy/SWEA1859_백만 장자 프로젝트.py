T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    now = lst[-1]
    for i in lst[-2::-1]:
        if i < now:
            ans += (now-i)

        else:
            now = i

    print(f"#{tc} {ans}")
