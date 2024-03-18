import sys
sys.stdin = open('../a.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for i in B:
        S = 0
        E = N - 1
        check = -1

        while S <= E:
            M = (S + E) // 2

            if A[M] == i:
                cnt += 1
                break

            elif A[M] < i:
                S = M + 1

                if check == 1:
                    break
                else:
                    check = 1

            else:
                E = M - 1

                if check == 0:
                    break
                else:
                    check = 0

    print(f"#{tc} {cnt}")
