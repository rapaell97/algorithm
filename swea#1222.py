for tc in range(1,11):
    T = int(input())
    lst = list(input())
    stack = list()
    op = 0
    for i in lst:
        if i.isdecimal() == True:
            stack.append(int(i))
        else:
            op += 1

        if op == 1 and len(stack) == 2:
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(temp1+temp2)
            op = 0

    print(f"#{tc}",*stack)



