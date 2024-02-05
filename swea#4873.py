test = int(input())
for u in range(test):
    lst = list()
    str = input()

    for i in str:
        if i in lst and lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)

    print(f"#{u+1} {len(lst)}")