num1=list(map(int,input()))
num2=list(map(int,input()))

sub_lst = list()
for i in range(8):
    sub_lst.append(num1[i])
    sub_lst.append(num2[i])

lst = [sub_lst]

i = 1
while len(lst[-1]) > 2:
    sub_lst2 = []
    for k in range(len(lst[i - 1]) - 1):
        sub_lst2.append((lst[i - 1][k] + lst[i - 1][k + 1]) % 10)
    lst.append(sub_lst2)
    i += 1

for i in lst[-1]:
    print(i,end='')



