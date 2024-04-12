import sys
sys.stdin = open('a.txt', 'r')

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

ans = K ** 2
for i in range(M-K+1):
    for j in range(N-K+1):
        BS = 0
        WS = 0
        print(f"i:{i} j{j} 탐색 시작")

        print('############BLACK#############')
        for p in range(i, i+K):
            for q in range(j, j+K):
                print(p,q)
                if p % 2 == 0:
                    if q % 2 == 0:
                        if board[p][q] != 'B':
                            BS += 1
                    else:
                        if board[p][q] != 'W':
                            BS += 1

                else:
                    if q % 2 == 0:
                        if board[p][q] != 'W':
                            BS += 1
                    else:
                        if board[p][q] != 'B':
                            BS += 1

        print('############WHITE#############')
        for p in range(i, i+K):
            for q in range(j, j+K):
                print(p,q)
                if p % 2 == 0:
                    if q % 2 == 0:
                        if board[p][q] != 'W':
                            WS += 1
                    else:
                        if board[p][q] != 'B':
                            WS += 1

                else:
                    if q % 2 == 0:
                        if board[p][q] != 'B':
                            WS += 1
                    else:
                        if board[p][q] != 'W':
                            WS += 1

        ans = min(ans, BS, WS)

print(ans)




