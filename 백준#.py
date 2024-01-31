num = int(input())
lst = [int(input()) for _ in range(num)]

counts = [0 for _ in range(10001)]

for i in lst:
    counts[i]+=1

for i in counts:
    if i != 0:
