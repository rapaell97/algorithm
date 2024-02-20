def inorder(t):
    if t:
        inorder(int(left[t]))
        print(arr[t], end='')
        inorder(int(right[t]))

for tc in range(1,11):
    N = int(input())
    lst = [[]]+[list(input().split()) for _ in range(N)]

    arr = [0 for _ in range(N+1)]

    left = [0 for _ in range(N+1)]
    right = [0 for _ in range(N+1)]

    for i in range(1,N + 1):
        if len(lst[i]) == 2:
            arr[i] = lst[i][1]
        if len(lst[i]) == 3:
            left[i] = lst[i][2]
            arr[i] = lst[i][1]
        if len(lst[i]) == 4:
            left[i] = lst[i][2]
            right[i] = lst[i][3]
            arr[i] = lst[i][1]
    print(f"#{tc}",end=' ')
    inorder(1)
    print()