# 1. 장애물 설치
# 2. 선생님 마다 학생 탐지
from itertools import combinations

# boolean 으로 return false false true false -> false
# def dfs(x, y, local_dx, local_dy):
#     nx = local_dx + x
#     ny = local_dy + y
#     print(nx, ny)
#     if 0 <= nx < n and 0 <= ny < n:
#         if field[nx][ny] == 'O':
#             return False
#         if field[nx][ny] == 'S':
#             return True
#         print(dfs(nx, ny, local_dx, local_dy))
#     return False


def check_direction(x, y, l_dx, l_dy):
    while (0 <= x < n and 0 <= y < n):
        if field[x][y] == 'S':
            return True
        if field[x][y] == 'O':
            return False
        x += l_dx
        y += l_dy
    return False


def detect():
    detected = False  # 탐지 안됨
    for x, y in teachers:
        # 4방향 검사
        for i in range(4):
            detected = check_direction(x, y, dx[i], dy[i])
            # 탐지 된 경우
            if detected:
                return detected

    return detected  # 탐지 안된 경우


n = int(input())
field = []
for _ in range(n):
    field.append(list(input().split()))

students = []
teachers = []
empty_areas = []
for i in range(n):
    for j in range(n):
        if field[i][j] == 'S':
            students.append((i, j))
        elif field[i][j] == 'T':
            teachers.append((i, j))
        else:
            empty_areas.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

detected = True
for case in combinations(empty_areas, 3):
    # 벽설치
    for x, y in case:
        field[x][y] = 'O'

    # 감지가 안된 경우
    if not detect():
        detected = False
        break

    # 지우기
    for x, y in case:
        field[x][y] = 'X'

if detected:
    print("NO")
else:
    print("YES")
