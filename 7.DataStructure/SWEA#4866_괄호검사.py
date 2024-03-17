import sys
sys.stdin = open('../a.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    line = input()

    check = True
    left = []
    for i in range(len(line)):
        if line[i] == '{' or line[i] == '(':
            left.append(line[i])

        elif line[i] == '}':
            if len(left) == 0:
                check = False
                break

            elif left[-1] == '{':
                left.pop()

            else:
                check = False
                break

        elif line[i] == ')':
            if len(left) == 0:
                check = False
                break

            elif left[-1] == '(':
                left.pop()

            else:
                check = False
                break

    if len(left) != 0:
        check = False

    if check:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
