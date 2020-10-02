from copy import deepcopy

arr = [[None]*4 for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        # (번호, 방향)
        arr[i][j] = [row[j*2], row[j*2+1]-1]

dirs = [(-1, 0), (-1, -1), (0, -1),
        (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction+1) % 8

# 특정 번호 물고기 찾기
def find_fish(arr, idx):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == idx:
                return (i,j)
    return None

# 모든 물고기 회전 및 이동 - (arr, 상어위치)
def move_all_fishes(arr, now_r, now_c):
    for i in range(1, 17):
        position = find_fish(arr, i)
        if position != None:
            r, c = position[0], position[1]
            direction = arr[r][c][1]

            # 물고기 회전하며 이동가능하지 확인
            for j in range(8):
                dr, dc = dirs[direction]
                nr, nc = dr + r, dc + c
                # 이동 가능한 경우 이동
                if 0 <= nr < 4 and 0 <= nc < 4:
                    if not (nr == now_r and nc == now_c):
                        arr[r][c][1] = direction
                        arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                        break
                direction = turn_left(direction)

# 상어가 먹을 수 있는 물고기 위치 반환
def can_eat_fishes(arr, now_r, now_c):
    fishes = []
    direction = arr[now_r][now_c][1]

    # 현재 방향으로 계속 이동
    for i in range(4):
        dr, dc = dirs[direction]
        now_r, now_c = dr+now_r, dc+now_c
        # 범위를 벗어나는지 확인
        if 0 <= now_r < 4 and 0 <= now_c <4:
            # 물고기 존재시
            if arr[now_r][now_c][0] != -1:
                fishes.append((now_r, now_c))
    return fishes

# 모든 경우 탐색
def dfs(arr, now_r, now_c, total):
    global result
    arr = deepcopy(arr)

    total += arr[now_r][now_c][0] # 현재 위치 물고기 먹기
    arr[now_r][now_c][0] = -1 # 물고기 먹은 후 -1

    move_all_fishes(arr, now_r, now_c)

    # 상어가 이동가능한 위치 찾기
    fishes = can_eat_fishes(arr, now_r, now_c) 
    
    if not fishes:
        result = max(result, total)
        return
    
    for next_r, next_c in fishes:
        dfs(arr, next_r, next_c, total)


result = 0
dfs(arr, 0, 0, 0)
print(result)
