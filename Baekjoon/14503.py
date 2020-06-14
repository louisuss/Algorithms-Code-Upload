from collections import deque

n, m = map(int, input().split())

# 행(세로) / 열(가로)
# position[2] = 방향 (0,1,2,3 / 북,동,남,서)
y, x, direction = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
# 0 1 2 3

# 한칸 전진을 위한 dy, dx
dirs = [(0,-1), (-1,0), (0,1), (1,0)]

# 후진을 위한 dy, dx
back = {0: (1,0), 1: (0,-1), 2: (-1,0), 3: (0,1)}

def bfs(start, map_list):
    queue = deque()
    queue.append(start)

    # 청소기가 청소한 횟수
    cnt = 0
    while queue:
        y, x, direction = queue.popleft()
        if map_list[y][x] == 0:
            # 청소한 좌표는 2로 지정
            map_list[y][x] = 2
            cnt += 1
        dy, dx = dirs[direction]

        # 왼쪽 이동했을 때 좌표
        nx = x + dx
        ny = y + dy

        # 바라보는 곳을 기준으로 후진해야 되는 위치 좌표
        by, bx = back[direction]

        # 더 이상 움직일 수 없는 경우
        cant_move = True
        for ty, tx in dirs:
            # 청소할 곳이 있으면 움직임
            if map_list[y+ty][x+tx] == 0:
                cant_move = False
                break

        if 0 <= ny < n and 0 <= nx < m:
            # a
            if map_list[ny][nx] == 0:
                new_direction = (direction-1)%4
                queue.append((ny,nx,new_direction))
            elif cant_move:
                # d
                if map_list[y+by][x+bx] == 1:
                    break
                # c
                else:
                    queue.append((y+by, x+bx, direction))
            else:
                # b
                new_direction = (direction-1)%4
                queue.append((y,x,new_direction))

    return cnt

print(bfs((y,x,direction), map_list))


