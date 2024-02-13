N = int(input())
lst = list()
for i in range(N):
    a = int(input())
    lst.append(a)

stack = []
i = 1
index = 0
ans = list()
check = True
while True:
    if lst[index] > i:
        stack.append(i)
        ans.append('+')
    elif lst[index] == i:
        stack.pop()
        ans.append('-')
    else: # lst[index] < i
        if lst[index] in stack:
            while True:
                temp = stack.pop()
                ans.append('-')
                if temp == lst[index]:
                    break
        else:
            check = False
            break
    i += 1

    if check:
        for i in ans:
            print(i)
    else:
        print('NO')






