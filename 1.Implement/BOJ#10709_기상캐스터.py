import sys
sys.stdin = open('../a.txt', 'r')

H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

for i in range(H):
    check = False
    for k in range(W):
        if arr[i][k] == 'c':
            arr[i][k] = 0
            temp = 1
            check = True

        elif arr[i][k] == '.':
            if check:
                arr[i][k] = temp
                temp += 1
            else:
                arr[i][k] = -1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()