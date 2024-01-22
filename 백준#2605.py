num = int(input())
line = list(map(int,input().split()))
new_line = list()

for i in range(len(line)):
    new_line.insert(line[i],i+1)

print(*new_line[::-1])
