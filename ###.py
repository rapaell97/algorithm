import sys
sys.stdin = open('a.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stop = [0] * 5001

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            stop[j] += 1

    P = int(input())
    print(f"#{tc}", end=' ')
    for i in range(P):
        a = int(input())
        print(stop[a], end=' ')

    print()




