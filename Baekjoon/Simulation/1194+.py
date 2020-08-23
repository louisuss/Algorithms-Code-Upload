from collections import deque

N, M = map(int, input().split())
fields = [list(input()) for _ in range(N)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
check = [[[0]*64 for _ in range(M)] for _ in range(N)]


# 1. 열쇠가 6개므로 2진법으로(0~111111)까지 표현가능하므로 열쇠에 해당하는 차수를 64로 설정

# 2. 이동 중에 소문자를 만나면 or 연산으로 열쇠 보유를 갱신하여 큐에 입력

# 3. 대문자를 만나면 and 연산으로 알맞은 열쇠를 보유했는지 체크 후 이동

# 4. 1을 만나면 이동 경로를  출력
def bfs(y, x):
    q = deque([[y, x, 0]])
    check[y][x][0] = 1

    while q:
        y, x, k = q.popleft()
        if fields[y][x] == '1':
            print(check[y][x][k] - 1)
            return
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                # 벽이 아니고
                if fields[ny][nx] != '#' and check[ny][nx][k] == 0:
                    # 키인 경우
                    if fields[ny][nx].islower():
                        # 키 추가
                        nk = k | (1 << (ord(fields[ny][nx]) - ord('a')))
                        if check[ny][nx][nk] == 0:
                            # 이전값 + 1
                            check[ny][nx][nk] = check[y][x][k] + 1
                            q.append([ny, nx, nk])
                    # 문인 경우
                    elif fields[ny][nx].isupper():
                        # 열쇠 있는 경우
                        if k & (1 << (ord(fields[ny][nx])-ord('A'))):
                            # 이동
                            check[ny][nx][k] = check[y][x][k] + 1
                            q.append([ny, nx, k])
                    # 이동 가능한 경우
                    else:
                        check[ny][nx][k] = check[y][x][k] + 1
                        q.append([ny, nx, k])
    print(-1)


for i in range(N):
    for j in range(M):
        if fields[i][j] == '0':
            bfs(i, j)
