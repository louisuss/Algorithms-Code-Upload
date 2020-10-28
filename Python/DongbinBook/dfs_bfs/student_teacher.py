# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# 4
# S S S T
# X X X X
# X X X X
# T T T X

from itertools import combinations
from copy import deepcopy

n = int(input())

# 우좌하상
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(new_field, student, dir, n):
    nr, nc = student[0] + dir[0], student[1] + dir[1]
    if 0 <= nr < n and 0 <= nc < n:
        if new_field[nr][nc] == 'O':
            return False
        elif new_field[nr][nc] == 'T':
            return True
        else:
            dfs(new_field, (nr, nc), dir, n)
    else:
        return False


field = [list(input().split()) for _ in range(n)]
empty_field = []
students = []
teachers = []
for i in range(n):
    for j in range(n):
        if field[i][j] == 'X':
            empty_field.append((i, j))
        if field[i][j] == 'S':
            students.append((i, j))
        if field[i][j] == 'T':
            teachers.append((i,j))

cases = list(combinations(empty_field, 3))

# Solution 1 - Student 기준
answer = False
for case in cases:
    # 걸리는 경우 확인위한 변수
    check = True
    new_field = deepcopy(field)

    # 벽 생성
    for c in case:
        new_field[c[0]][c[1]] = 'O'

    # 학생 별 4방향 체크
    for student in students:
        # 각 방향에 대해 dfs 진행
        for dir in dirs:
            # 걸리는 경우
            if dfs(new_field, student, dir, n):
                check = False
                break
        # 걸리는 경우 다음 경우의 수 진행
        if not check:
            break

    # 학생 전부 안걸리는 경우
    if check:
        print("YES")
        answer = True
        break

if not answer:
    print("NO")

# Solution 2 - Teacher 기준

dirs = {
    0: (0,-1),
    1: (0,1),
    2: (-1,0),
    3: (1,0)
}
def watch(r, c, dir):
    # 왼쪽 체크
    if dir == 0:
        while c >= 0:
            if field[r][c] == 'S':
                return True
            if field[r][c] == 'O':
                return False
            c -= 1
    # 오른쪽 체크
    elif dir == 1:
        while c < n:
            if field[r][c] == 'S':
                return True
            if field[r][c] == 'O':
                return False
            c += 1
    
    elif dir == 2:
        while 0 <= r:
            if field[r][c] == 'S':
                return True
            if field[r][c] == 'O':
                return False
            r -= 1
    elif dir == 3:
        while n > r:
            if field[r][c] == 'S':
                return True
            if field[r][c] == 'O':
                return False
            r += 1
    return False
        
def process():
    for r, c in teachers:
        # 좌우상하
        for dir in dirs:
            if watch(r, c, dir):
                return True
    return False

find = False # 학 생이 한명도 감지되지 않도록 설치할 수 있느 경우
for case in cases:
    for r, c in case:
        field[r][c] = 'O'
    
    # 원하는 경우 발견
    if not process():
        find = True
        break
    
    # 원상복구
    for r, c in case:
        field[r][c] = 'X'
if find:
    print("YES")
else:
    print("NO")

