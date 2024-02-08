# 별다른 조건없이 연결된 경우이기 때문에 양방향임
# com1,com2 com2,com1 모두 바이러스 감염 경로임
v = int(input())
e = int(input())
kill = [0 for _ in range(v+1)]
lst = [[0 for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    com1,com2 = map(int,input().split())
    lst[com1][com2] = 1
    lst[com2][com1] = 1

def dfs(computer):
    kill[computer] = 1

    for i in range(v+1):
        if kill[i] == 0 and lst[computer][i] == 1:
            dfs(i)

dfs(1)
print(kill.count(1)-1)