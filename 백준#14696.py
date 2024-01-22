round = int(input())
acard=list()
bcard=list()


for i in range(2*round):
    a = list(map(int,input().split()))
    if i % 2 == 0:
        acard.append(a)
    else:
        bcard.append(a)


for k in range(round):
    if acard[k][1:].count(4) > bcard[k][1:].count(4):
        print("A")
    elif acard[k][1:].count(4) == bcard[k][1:].count(4):
        if acard[k][1:].count(3) > bcard[k][1:].count(3):
            print("A")
        elif acard[k][1:].count(3) == bcard[k][1:].count(3):
            if acard[k][1:].count(2) > bcard[k][1:].count(2):
                print("A")
            elif acard[k][1:].count(2) == bcard[k][1:].count(2):
                if acard[k][1:].count(1) > bcard[k][1:].count(1):
                    print("A")
                elif acard[k][1:].count(1) == bcard[k][1:].count(1):
                    print("D")
                else:
                    print("B")
            else:
                print("B")
        else:
            print("B")
    else:
        print("B")
