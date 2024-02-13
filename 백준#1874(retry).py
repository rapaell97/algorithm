N = int(input())
stack = list()
check = True
point = 1
ans = list()
for u in range(N):
    num = int(input())
    while point <= num:
        stack.append(point)
        ans.append('+')
        point += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        check = False
        break
if check:
    for i in ans:
        print(i)
else:
    print('NO')