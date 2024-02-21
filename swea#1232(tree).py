def postorder(t):
    if t:
        postorder(left[t])
        postorder(right[t])
        if tree[t] == '+':
            tree[t] = tree[left[t]] + tree[right[t]]
        elif tree[t] == '-':
            tree[t] = tree[left[t]] - tree[right[t]]
        elif tree[t] == '*':
            tree[t] = tree[left[t]] * tree[right[t]]
        elif tree[t] == '/':
            tree[t] = tree[left[t]] / tree[right[t]]

for tc in range(1,11):
    case = int(input())
    tree = [0 for _ in range(case+1)]
    left = [0 for _ in range(case+1)]
    right = [0 for _ in range(case+1)]

    for i in range(1,case+1):
        temp = list(input().split())
        if len(temp) == 4:
            tree[int(temp[0])] = temp[1]
            left[int(temp[0])] = int(temp[2])
            right[int(temp[0])] = int(temp[3])
        else:
            tree[int(temp[0])] = int(temp[1])

    postorder(1)
    print(f"#{tc} {int(tree[1])}")