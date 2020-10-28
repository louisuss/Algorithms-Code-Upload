from collections import deque

# Solution1
INF = 1e9

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

baby_shark = 2
now_r, now_c = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            now_r, now_c = i, j
            board[now_r][now_c] = 0
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# 모든 위치까지의 최단거리 구하기


def find_dist():
    # 값이 -1이면 도달할 수 없음 의미
    dist = [[-1]*n for _ in range(n)]
    # 시작위치는 도달이 가능하다고 보며 거리 = 0
    q = deque([(now_r, now_c)])
    dist[now_r][now_c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nr][nc] == -1 and board[nr][nc] <= baby_shark:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    return dist

# 최단 거리 테이블에서 먹을 물고기 찾기


def find_fish(dist):
    r, c = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기인 경우
            if dist[i][j] != -1 and 1 <= board[i][j] < baby_shark:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    r, c = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:  # 먹을 수 있는 물고기 없는 경우
        return None
    else:
        return r, c, min_dist  # 먹을 물고기 위치, 최단거리


result = 0
ate = 0  # 먹은 물고기 수 (사이즈 증가위해)
while True:
    # 먹을 수 있는 물고기 찾기
    fish = find_fish(find_dist())
    if fish == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_r, now_c = fish[0], fish[1]
        result += fish[2]
        board[now_r][now_c] = 0
        ate += 1
        if ate >= baby_shark:
            baby_shark += 1
            ate = 0


# Solution2
# bfs -> 임의 리스트에 누적 거리로 표시, 단순 방문정보 표시 따로 거리 따로 계산하지 않기

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
baby_shark = 2  # 아기 상어 크기
now = []  # 아기 상어 위치
fishes = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            now = [i, j]
            board[i][j] = 0
        if 1 <= board[i][j] <= 6:
            fishes.append((i, j))


def close_fish(arr):
    arr = sorted(arr, key=lambda x: (x[0], x[1]))
    return arr[0]


def find_fish(row, col, n):
    q = deque([(row, col)])
    visited = [[-1]*n for _ in range(n)]  # 중복 제거
    visited[row][col] = 0

    while q:
        r, c = q.popleft()  # 현재 위치

        can_eat = []  # 먹을 수 있는 먹이 리스트
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                # 이동 가능한 경우 큐에 넣기
                if board[nr][nc] <= baby_shark:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                # 먹을 수 있는 경우, 먹이 리스트 추가
                if 1 <= board[nr][nc] < baby_shark:
                    can_eat.append((nr, nc))

        cnt_eat = len(can_eat)
        # 먹을 수 있는 물고기가 없는 경우 위치 이동
        if cnt_eat == 0:
            continue
        # 1마리
        elif cnt_eat == 1:
            fish_r, fish_c = can_eat[0][0], can_eat[0][1]
            return ((fish_r, fish_c), visited[fish_r][fish_c])
        # 2마리 이상
        else:
            fish_r, fish_c = close_fish(can_eat, (row, col))
            # 가장 가까운 위에 왼쪽 물고기 먹기, 그 물고기까지 거리
            return ((fish_r, fish_c), visited[fish_r][fish_c])


ate = 0
distance = 0

while True:
    fish = find_fish(now[0], now[1], n)

    if fish == None:
        break
    else:
        now = fish[0]  # 먹는 물고기 위치로 이동

        distance += fish[1]  # 이동 거리 추가
        ate += 1  # 이동 물고기 추가
        # 먹은 물고기수가 아기 상어 크기인 경우
        if ate == baby_shark:
            baby_shark += 1
            ate = 0
        board[now[0]][now[1]] = 0

print(distance)
