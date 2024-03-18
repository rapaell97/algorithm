import sys
input = sys.stdin.readline
sys.stdin = open('../a.txt', 'r')
while True:
    try:
        X = int(input()) * 10000000
        N = int(input())

        lego = [int(input()) for _ in range(N)]
        lego.sort()

        S = 0
        E = N - 1

        check = False
        while S < E:
            temp = (lego[S] + lego[E])

            if temp == X:
                check = True
                print(f"yes {lego[S]} {lego[E]}")
                break

            elif temp < X:
                S += 1

            else:
                E -= 1

        if not check:
            print('danger')

    except:
        break
