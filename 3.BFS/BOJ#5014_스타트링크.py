import sys
sys.stdin = open ('../my_input.txt', 'r')
from collections import deque

def bfs(i):
    visit = [0] * (F + 1)
    visit[i] = 1
    queue = deque()
    queue.append(i)
    turn = 0

    while queue:
        for _ in range(len(queue)):
            i = queue.popleft()

            if i == G:
                print(turn)
                return

            for j in range(2):
                ni = i + move[j]

                if 1<= ni <(F + 1) and visit[ni] == 0:
                    visit[ni] = 1
                    queue.append(ni)
        turn += 1

    else:
        print('use the stairs')


F, S, G, U, D = map(int, input().split())

building = [0] * (F + 1)
move = [U, -D]
bfs(S)