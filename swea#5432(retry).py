tc = int(input())
for u in range(tc):
    lst = list(input())
    stack = list()
    ans = 0

    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append(lst[i])
        else:
            if lst[i-1] == '(':
                stack.pop()
                ans+=len(stack)
            else:
                stack.pop()
                ans+=1
    print(f"#{u+1} {ans}")
