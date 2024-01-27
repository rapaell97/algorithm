a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list()
for i in range(5):
    x=a[i]*b[i]+c[i]
    d.append(x)
print(*d)
