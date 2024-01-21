a_card=list(map(int,input().split()))
b_card=list(map(int,input().split()))
a_win=list()
b_win=list()

for i in range(10):
    if a_card[i]>b_card[i]:
        a_win.append(3)
        b_win.append(0)
    elif a_card[i]==b_card[i]:
        a_win.append(1)
        b_win.append(1)
    else:
        b_win.append(3)
        a_win.append(0)

print(sum(a_win),sum(b_win))

if sum(a_win) > sum(b_win):
    print("A")
elif sum(a_win) == sum(b_win):
    if a_win == b_win:
        print("D")
    else:
        for k in range(8,-1,-1):
            if a_win[k] != b_win[k]:
                if a_win[k]>b_win[k]:
                    print("A")
                    break
                else:
                    print("B")
                    break
else:
    print("B")
