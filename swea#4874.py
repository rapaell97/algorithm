tc = int(input())
for u in range(tc):
    case = list(input().split())
    stack = list()

    for i in range(len(case)):
        if case[i].isdecimal() == True:
            stack.append(case[i])

        elif case[i] == '+':
            if len(stack) < 2:
                print(f"#{u + 1} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp2 + temp1)

        elif case[i] == '/':
            if len(stack) < 2:
                print(f"#{u + 1} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp2 // temp1)

        elif case[i] == '*':
            if len(stack) < 2:
                print(f"#{u + 1} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp2 * temp1)

        elif case[i] == '-':
            if len(stack) < 2:
                print(f"#{u + 1} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp2 - temp1)

        elif case[i] == '.':
            if len(stack) == 1:
                print(f"#{u + 1} {stack[0]}")
            else:
                print(f"#{u + 1} error")
            break
