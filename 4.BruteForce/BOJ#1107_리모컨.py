N = int(input())
M = int(input())

if M == 0:
    button_x = []
else:
    button_x = list(input().split())

ans = 21e8
for i in range(1000000):
    temp = str(i)
    size = len(temp)

    check = True
    for j in range(size):
        if temp[j] in button_x:
            check = False
            break

    if check:
        temp_ans = size + abs(i - N)
        ans = min(temp_ans, ans)

ans = min(ans, abs(100 - N))
print(ans)

