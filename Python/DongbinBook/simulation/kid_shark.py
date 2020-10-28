# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2

# 12 6 14 5 4 5 6 7
# 15 1 11 7 3 7 7 5
# 10 3 8 3 16 6 1 1
# 5 8 2 7 13 6 9 2
from copy import deepcopy

board = [[] for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0, 8, 2):
        # (번호, 방향)
        board[i].append((row[j], row[j+1]))

dirs = [(0, 0), (-1, 0), (-1, -1), (0, -1),
        (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# 번호가 작은 순서로 이동하기 위해 번호에 해당하는 물고기 위치 찾기 함수


def find_fish_number(board, number):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 1 or board[i][j] == 0:
                continue

            if board[i][j][0] == number:
                return (i, j)

# 재귀 구현시 헷갈림


def rotate_fish(board, pos, dir):
    new_dir = dir + 1
    if new_dir > 8:
        new_dir = new_dir % 8

    while dir != new_dir:
        check = move_fish(board, pos, new_dir)
        # 이동 가능한 경우 종료
        if check:
            break
        else:
            new_dir += 1
            if new_dir > 8:
                new_dir = new_dir % 8


def move_fish(board, pos, dir):
    now_r, now_c = pos  # 현재 위치
    dr, dc = dirs[dir]
    nr, nc = dr+now_r, dc+now_c  # 이동할 위치

    # 범위안에 있고 상어가 없는 경우
    if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc] != 1:
        # 물고기가 있는 경우 - 위치 변경
        if board[nr][nc]:
            # swap
            board[nr][nc], board[now_r][now_c] = board[now_r][now_c], board[nr][nc]
        else:  # board[nr][nc] == 0
            board[nr][nc] = board[now_r][now_c]
            board[now_r][now_c] = 0
        return True
    # 이동 못하는 경우 - 회전 후 이동
    # 재귀 구현시 헷갈림. 여기서 rotate 함수 호출의 경우
    else:
        return False


# 물고기 이동 함수
def total_move_fish(board):
    for number in range(1, 17):  # 1~16
        position = find_fish_number(board, number)  # 해당 번호 물고기 찾기
        if position == None:
            continue
        check = move_fish(
            board, position, board[position[0]][position[1]][1])  # 물고기 이동
        # 물고기 이동 실패 시 45도 이동하면 이동가능 위치 찾기
        if not check:
            rotate_fish(board, position,
                        board[position[0]][position[1]][1])


# 상어의 방향에 있는 물고기 리스트

def can_eat_fishes(board, now, dir):
    r, c = now[0], now[1]
    fishes = []
    dr, dc = dirs[dir]

    for i in range(4):
        r, c = r + dr, c + dc
        if 0 <= r < 4 and 0 <= c < 4:
            if board[r][c]:
                fishes.append((r, c))
    return fishes


# 결과값 오류
def dfs(board, r, c, total):
    global result
    board = deepcopy(board)

    total += board[r][c][0]
    direction = board[r][c][1]
    board[r][c] = 0

    total_move_fish(board)

    fishes = can_eat_fishes(board, (r, c), direction)

    if not fishes:
        result = max(result, total)
        return

    for next_r, next_c in fishes:
        dfs(board, next_r, next_c, total)


result = 0
dfs(board, 0, 0, 0)
print(result)
