def bk(i, queen): # i : i번째 행에 퀸을 놓을 지 말지 정하는 작업
    global cnt
    if queen == N and i == N: # 1 종료 조건
        cnt += 1
        return

    # 2 재귀 호출
    # i번째 행에 대해 퀸을 놓을 수 있는지 판단
    # 놓을 수 있다면 놓고, i+1번째 행으로 퀸을 놓으러 감

    for k in range(N): # 현재 i번째 행에서 k번 열에다가 놓아보겠다.
        check = True
        # 판단 케이스 => 세로 , 대각에 이전에 놓은 퀸이 있는지 확인
        for j in range(i): # 세로
            if visit[j][k] == 1:
                check = False
                break
        for j in range(1, i+1):
            if i - j >= 0 and k - j >= 0 and visit[i-j][k-j] == 1: # 좌측 대각선
                check = False
                break
            if i - j >= 0 and k + j < N and visit[i-j][k+j] == 1: # 우측 대각선
                check = False
                break

        if check:
            visit[i][k] = 1
            bk(i+1, queen+1)
            visit[i][k] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visit = [[0 for _ in range(N)] for _ in range(N)] # 체스판
    cnt = 0 # 퀸을 놓을 수 있는 경우의 수
    bk(0, 0)
    print(f"#{tc} {cnt}")


