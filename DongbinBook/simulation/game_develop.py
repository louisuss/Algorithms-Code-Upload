# My Solution
n, m = map(int, input().split())
now_row, now_col, direction = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[now_row][now_col] = 1
dirs = {
    0: (-1,0),
    1: (0,1),
    2: (1,0),
    3: (0,-1)
}


def change_direction(direction):
    if direction == 0:
        dir = 3
    else:
        dir = direction - 1
    return dir

count = 1

while True:
    possible = False
    for i in range(4):
        rotate_direction = change_direction(direction)
        row, col = dirs[rotate_direction]
        new_row, new_col = now_row + row, now_col + col
        if not visited[new_row][new_col] and not field[new_row][new_col]:
            possible = True
            visited[new_row][new_col] = 1
            count += 1
            now_row, now_col = (new_row, new_col)
            direction = rotate_direction
            break
        direction = rotate_direction

    if not possible:
        row, col = dirs[direction]
        new_row, new_col = now_row - row, now_col - col

        if field[now_row][now_col]:
            break
        else:
            now_row, now_col = new_row, new_col

print(count)

# Book Solution
# n, m = map(int, input().split())

# d = [[0]*m for _ in range(n)]
# x, y, direction = map(int,input().split())
# d[x][y] = 1

# arr = [list(map(int, input().split())) for _ in range(n)]
# # 북, 동, 남, 서
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# # 왼쪽 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]

#     if d[nx][ny] == 0 and arr[nx][ny] == 0:
#         d[nx][ny] = 1
#         x, y = nx, ny
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dx[direction]

#         if arr[nx][ny] == 0:
#             x, y = nx, ny
#         else:
#             break
#         turn_time = 0
# print(count)