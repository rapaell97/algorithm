from collections import deque
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

def bfs(i, k):
    global ans
    queue = deque()
    queue.append((i, k))

    while queue:
        i, k, cnt = queue.popleft()

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0<= ni <N and 0<= nk <N:
                pass
                # if time_spend[0][0] + lst[]:
                #     queue.append((i, k))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]

    time_spend = [[]]
    #https: // mungto.tistory.com / 224
    #https: // hyunse0.tistory.com / 350?category = 995136


    bfs(0,0)

    print(f"#{tc} {ans}")
