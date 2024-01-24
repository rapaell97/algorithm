from collections import deque
lst = deque()
yose = list()
n,k = list(map(int,input().split()))
for i in range(1,n+1):
    lst.append(i)

while lst:
    for q in range(k-1):
        x = lst.popleft()
        lst.append(x)
    y = lst.popleft()
    yose.append(y)

result = str(yose).replace('[','<').replace(']','>')
print(result)
