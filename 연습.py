lst = input().split()

def checkChar(x):
    if ord(x)>=97 and ord(x)<=122:
        print("소",end='')
    else:
        print("대",end='')

for i in lst:
    checkChar(i)