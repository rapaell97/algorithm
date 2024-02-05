def password(pw):
    lst = list()
    for i in pw:
        if i in lst and lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)

    return lst

for tc in range(10):
    num,pw = input().split()
    print(f"#{tc+1}",''.join(password(pw)))