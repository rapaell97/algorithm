tc = int(input())
for u in range(tc):
    case = list(input().split())
    stack = list()

    for i in range(len(case)):
        if case[i].isdecimal() == True:
            stack.append(case[i])

        elif case[i] == '+':
            if len(stack)<2:
                print(f"#{u} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                temp3 = temp1 + temp2
                stack.append(temp3)

        elif case[i] == '/':
            if len(stack)<2:
                print(f"#{u} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                temp3 = temp2 // temp1
                stack.append(temp3)

        elif case[i] == '*':
            if len(stack)<2:
                print(f"#{u} error")
                break
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                temp3 = temp1 * temp2
                stack.append(temp3)

        elif case[i] == '.':
            print(f"#{u} {temp3}")
            break

