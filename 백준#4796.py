lst = list()
while True:
    sub_list = list(map(int,input().split()))
    if sub_list[0]==0 and sub_list[1]==0 and sub_list[2]==0:
        break
    else:
        lst.append(sub_list)

for i in range(len(lst)):
    a,b=divmod(lst[i][2],lst[i][1])
    if b>lst[i][0]:
        day = (lst[i][0]*a)+lst[i][0]
    else:
        day = (lst[i][0]*a)+b
    print(f"Case {i+1}: {day}")



