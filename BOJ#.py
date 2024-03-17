def VS(A, B):
    for i in range(4, 0, -1):
        CA = A.count(i)
        CB = B.count(i)

        if CA == CB:
            continue
        else:
            if CA > CB:
                print('A')
                return
            else:
                print('B')
                return
    print('D')

T = int(input())
for tc in range(T):
    A = list(map(int, input().split()))
    A.pop(0)
    B = list(map(int, input().split()))
    B.pop(0)

    VS(A, B)

