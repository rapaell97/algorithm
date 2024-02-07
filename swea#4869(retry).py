tc = int(input())
for u in range(tc):
    num = int(input())
    lst = [1,3]
    for i in range(2,(num//10)):
        lst.append(lst[i-1]+2*lst[i-2])

    print(f"#{u+1} {lst[-1]}")