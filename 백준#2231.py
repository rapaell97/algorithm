num = int(input())
x = 0
check = False
while x <= num:
    str_x = str(x)
    temp = 0
    for i in str_x:
        temp+=int(i)
    if x + temp == num:
        check = True
        break
    x+=1

if check:
    print(x)
else:
    print(0)
