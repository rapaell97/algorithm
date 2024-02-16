def dfs(x, y, chance, cnt):
    global max_length
    max_length = max(max_length, cnt)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if board[nx][ny] < board[x][y]:  # 낮은 지형으로 이동
                visited[nx][ny] = True
                dfs(nx, ny, chance, cnt + 1)
                visited[nx][ny] = False
            elif chance and board[nx][ny] - K < board[x][y]:  # 지형을 깎을 수 있는 경우
                original = board[nx][ny]
                board[nx][ny] = board[x][y] - 1  # 지형 깎기
                visited[nx][ny] = True
                dfs(nx, ny, 0, cnt + 1)
                board[nx][ny] = original  # 원상 복구
                visited[nx][ny] = False

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    max_height = max(map(max, board))  # 최고 높이 구하기

    highest_spots = []  # 가장 높은 봉우리의 위치 저장
    for i in range(N):
        for j in range(N):
            if board[i][j] == max_height:
                highest_spots.append((i, j))

    for x, y in highest_spots:  # 가장 높은 봉우리들에서 DFS 시작
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True
        dfs(x, y, 1, 1)

    print(f"#{tc} {max_length}")