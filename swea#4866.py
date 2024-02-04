test = int(input())
for u in range(test):
    case = list(input())
    left = list()

    check = True
    for i in range(len(case)):
        if case[i] == '(' or case[i] == '{':
            left.append(case[i])
        if case[i] == ')':
            if len(left) == 0:
                check = False
                break
            elif left[-1] != '(':
                check = False
                break
            else:
                left.pop()

        if case[i] == '}':
            if len(left) == 0:
                check = False
                break
            elif left[-1] != '{':
                check = False
                break
            else:
                left.pop()

    if not check or len(left) != 0:
        print(f"#{u+1} 0")
    else:
        print(f"#{u+1} 1")

