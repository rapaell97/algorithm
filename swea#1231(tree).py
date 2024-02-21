def inorder(t):
    if t:
        inorder(int(left[t]))
        ans_lst.append(tree[t])
        inorder(int(right[t]))

for tc in range(1,11):
    N = int(input())
    left = [0 for _ in range(N+1)]
    right = [0 for _ in range(N+1)]
    tree = [0 for _ in range(N+1)]
    ans_lst = list()

    for i in range(1,N+1):
        temp = list(input().split())
        tree[i] = temp[1]
        if len(temp) == 3:
            left[i] = int(temp[2])
        if len(temp) == 4:
            left[i] = int(temp[2])
            right[i] = int(temp[3])

    inorder(1)
    print(ans_lst)





