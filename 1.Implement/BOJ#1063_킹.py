import sys
sys.stdin = open('../a.txt', 'r')

move = {'R': [0, 1], 'L': [0, -1], 'B': [-1, 0], 'T': [1, 0],
        'RT': [1, 1], 'LT': [1, -1], 'RB': [-1, 1], 'LB': [-1, -1]
        }
alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
arr = [[0] * 9 for _ in range(9)]

king, doll, N = input().split()
arr[int(king[1])][alpha[king[0]]] = 1
arr[int(doll[1])][alpha[doll[0]]] = 2

for turn in range(int(N)):

    for i in range(9):
        for k in range(9):
            if arr[i][k] == 1:
                king_i = i
                king_k = k
            elif arr[i][k] == 2:
                doll_i = i
                doll_k = k

    command = input()
    new_king_i = king_i + move[command][0]
    new_king_k = king_k + move[command][1]

    if 1<= new_king_i <9 and 1<= new_king_k <9:
        if arr[new_king_i][new_king_k] == 0:
            arr[new_king_i][new_king_k] = 1
            arr[king_i][king_k] = 0

        else:
            new_doll_i = doll_i + move[command][0]
            new_doll_k = doll_k + move[command][1]

            if 1<= new_doll_i <9 and 1<= new_doll_k <9:
                arr[new_doll_i][new_doll_k] = 2
                arr[doll_i][doll_k] = 1
                arr[king_i][king_k] = 0

for i in range(9):
    for k in range(9):
        if arr[i][k] == 1:
            ans_king_i = i
            ans_king_k = k
        elif arr[i][k] == 2:
            ans_doll_i = i
            ans_doll_k = k

print(chr(ans_king_k + 64), end='')
print(ans_king_i)
print(chr(ans_doll_k + 64), end='')
print(ans_doll_i)
