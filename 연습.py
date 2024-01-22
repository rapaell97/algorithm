def kfc(x):
    print(x*7)
def bbq(y):
    for i in range(y+1):
        print(i,end='')

num = int(input())
if num%2 == 0:
    k = input()
    kfc(k)
else:
    j = int(input())
    bbq(j)
