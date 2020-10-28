from collections import deque

N = int(input())
K = int(input())

# 지도
map_list = [[0]*N for _ in range(N)]

# 사과 위치
for _ in range(K):
    y, x = map(int, input().split())
    map_list[y-1][x-1] = 2

# 초 / 회전방향
L = int(input())
change = {}

for i in range(L):
    time, dir = map(str, input().split())
    change[int(time)] = dir

direction = 0
# 동 서 남 북
dirs = {0:(0,1),1:(0,-1),2:(1,0),3:(-1,0)}

def change_dir(direction, dir):
    y, x = dirs[direction]

    if direction == 0:
        if dir == 'D':
            return 2
        else:
            return 3
    elif direction == 1:
        if dir == 'D':
            return 3
        else:
            return 2
    elif direction == 2:
        if dir == 'D':
            return 1
        else:
            return 0
    else:
        if dir == 'D':
            return 0
        else:
            return 1

time = 0
y, x = 0, 0

snake = deque()
snake.append((y,x))

while True:
    time+=1
    dy, dx = dirs[direction]
    ny, nx = y + dy, x +dx

    # 보드 위에 있을 경우
    if 0 <= ny < N and 0 <= nx < N:
        # 사과인 경우
        if map_list[ny][nx] == 2:
            snake.appendleft((ny,nx))
            map_list[ny][nx] = 1

        # 빈 경우
        elif map_list[ny][nx] == 0:
            map_list[ny][nx] = 1
            snake.appendleft((ny,nx))
            tail_y, tail_x = snake.pop()
            map_list[tail_y][tail_x] = 0

        # 자기 몸에 부딪힌 경우
        elif map_list[ny][nx] == 1:
            break
        y, x = ny, nx

        # 방향 변환해야 하는 시간인 경우
        if time in change:
            direction = change_dir(direction, change[time])
    else:
        break
print(time)

