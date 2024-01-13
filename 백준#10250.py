t=int(input())
for i in range(t):
    a,b,c=list(map(int,input().split()))

    x=c%a
    y=c//a+1

    if x == 0:
        x=a
        y=c//a

    if y>=10:
        print(f'{x}{y}')
    else :
        print(f'{x}0{y}')

    
