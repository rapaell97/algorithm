def tournament(start, end):
    if start == end:
        return start

    a = tournament(start, (start + end) // 2)
    b = tournament((start + end) // 2 + 1, end)
    return rsp(a,  b)


def rsp(a, b):
    if lst[a] == lst[b]:
        return a
    if lst[a] > lst[b]:
        if lst[a] - lst[b] == 1:
            return a
        else:
            return b
    if lst[a] < lst[b]:
        if lst[b] - lst[a] == 1:
            return b
        else:
            return a


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f"#{tc} {tournament(0, N - 1) + 1}")
