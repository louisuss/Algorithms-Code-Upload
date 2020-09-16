# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
from collections import deque

# Solution 1
n = int(input())
k = int(input())
field = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    field[a][b] = 1

l = int(input())
direction = deque([])
for _ in range(l):
    x, c = list(input().split())
    direction.append((int(x), c))


dirs = {
    "r": (0, 1),
    "l": (0, -1),
    "u": (-1, 0),
    "d": (1, 0)
}
now_dir = "r"
snake_position = [[0]*(n+1) for _ in range(n+1)]
snake_lst = deque([])


def dir_choose(prev, change):
    dir = prev
    if prev == "r":
        if change == "D":
            dir = "d"
        else:
            dir = "u"
    elif prev == "l":
        if change == "D":
            dir = "u"
        else:
            dir = "d"
    elif prev == "u":
        if change == "D":
            dir = "r"
        else:
            dir = "l"
    elif prev == "d":
        if change == "D":
            dir = "l"
        else:
            dir = "r"

    return dir


def move_snake(head, tail, dir, length, time):
    # snake 위치 표시
    snake_position[head[0]][head[1]] = 1
    snake_position[tail[0]][tail[1]] = 1

    # 방향 설정
    dr, dc = dirs[dir]
    # 몸길이 늘리기. 머리이동
    new_head_r, new_head_c = head[0] + dr, head[1] + dc

    # 조건에 부합한 경우
    if 1 <= new_head_r < len(field) and 1 <= new_head_c < len(field):
        if snake_position[new_head_r][new_head_c] != 1:
            # 길이 시간 증가
            length += 1
            time += 1
            snake_lst.append((new_head_r, new_head_c))
            new_tail_r, new_tail_c = tail
            # 사과가 있는 경우
            if field[new_head_r][new_head_c] == 1:
                field[new_head_r][new_head_c] = 0
            # 사과 없는 경우
            else:
                length -= 1
                snake_position[tail[0]][tail[1]] = 0
                new_tail_r, new_tail_c = snake_lst.popleft()

            if time in list(a[0] for a in direction):
                change = direction.popleft()[1]
                dir = dir_choose(dir, change)

            return move_snake((new_head_r, new_head_c), (new_tail_r, new_tail_c), dir, length, time)
        else:
            return time + 1
    # 종료
    else:
        return time + 1


# print(move_snake((1, 1), (1, 1), "r", 1, 0))


# Solution 2

# 처음 오른쪽 (동, 남, 서, 북)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction


def simulate():
    r, c = 1, 1
    field[r][c] = 2
    dir = 0
    time = 0
    idx = 0  # 다음에 회전할 정보
    snake = deque([(r, c)])  # 뱀 위치 정보
    while True:
        nr, nc = r + dr[dir], c + dc[dir]
        if 1 <= nr <= n and 1 <= nc <= n and field[nr][nc] != 2:
            # 사과 없는 경우
            if field[nr][nc] == 0:
                # 뱀 머리 이동. 위치 추가
                field[nr][nc] = 2
                snake.append((nr, nc))
                # 뱀 꼬리 위치 변경
                tail_r, tail_c = snake.popleft()
                field[tail_r][tail_c] = 0
            # 사과 있는 경우
            if field[nr][nc] == 1:
                field[nr][nc] = 2
                snake.append((nr, nc))
        else:
            time += 1
            break
        r, c = nr, nc  # 다음 위치로 머리 이동
        time += 1

        if time == direction[idx][0]:
            dir = turn(dir, direction[idx][1])
            idx += 1
    return time

# print(simulate())
