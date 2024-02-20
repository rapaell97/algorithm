def preorder(t):
    global ans
    if t:
        ans += 1
        preorder(left[t])
        preorder(right[t])

T = int(input())
for tc in range(1,T+1):
    E , N = map(int,input().split())
    lst = list(map(int,input().split()))

    left = [0 for _ in range(E + 2)]
    right = [0 for _ in range(E + 2)]

    for i in range(E):
        p = lst[i * 2]
        c = lst[i * 2 + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    ans = 0
    preorder(N)
    print(f"#{tc} {ans}")



