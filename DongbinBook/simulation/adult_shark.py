# 4 2 6
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 2
# 4 3
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3

# 결과 에러
from copy import deepcopy

n, m, k = map(int, input().split())  # 판크기, 상어수, 냄새 초기화 시간
arr = [list(map(int, input().split())) for _ in range(n)]  # 상어 위치 표시
priority = [[] for _ in range(m+1)]  # 상어수 만큼 우선순위 표가 존재. (1~m). (위, 아래, 왼, 오)
directions = [0] + list(map(int, input().split()))  # 1~m
gas = [[[0, 0]] * n for _ in range(n)]

for i in range(1, m+1):
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))


def marking_gas(arr, k):
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                gas[i][j] = [arr[i][j], k]  # (번호, 초기시간)


def find_shark(arr):
    sharks_position = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                # 번호 순 정렬해서 사용하기 위해 필요
                sharks_position.append((arr[i][j], i, j))
    return sharks_position


dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def move_shark(arr, n):
    copy_arr = deepcopy(arr)
    sharks = find_shark(arr)

    # 위치가 중복되는 경우 번호가 낮은게 나중에 처리되어 덮어씀
    sharks.sort(reverse=True)

    for shark in sharks:
        shark_number, now_r, now_c = shark  # 현재상어 위치
        shark_dir = directions[shark_number]  # 현재 상어 방향

        # 현재 상어 방향 기준 우선순위 리스트
        priority_lst = priority[shark_number][shark_dir-1]

        # prev list
        prev_list = []
        check = False
        for dir in priority_lst:
            dr, dc = dirs[dir]  # 방향
            next_r, next_c = dr + now_r, dc + now_c  # 이동 위치

            # 벽이 아닌 경우
            if 0 <= next_r < n and 0 <= next_c < n:
                # 이동할 위치에 냄새가 없는 경우 (gas)
                if gas[next_r][next_c][1] == 0:
                    # 상어 이동 (이동하는 경우 이전경우가 덮어쓰는 경우가 있기 때문에 copy해서 사용)
                    copy_arr[next_r][next_c] = arr[now_r][now_c]
                    copy_arr[now_r][now_c] = 0
                    # 이동하는 방향으로 방향 변경
                    directions[shark_number] = dir
                    check = True
                    arr = copy_arr
                    break
                # 이전 위치로 이동하기 위해
                if arr[next_r][next_c][0] == shark_number:
                    prev_list.append([gas[next_r][next_c][1], dir])

        prev_list.sort(reverse=True)

        # 이전
        if not check:
            dr, dc = dirs[prev_list[0][1]]
            next_r, next_c = dr + now_r, dc + now_c
            copy_arr[next_r][next_c] = arr[now_r][now_c]
            copy_arr[now_r][now_c] = 0
            directions[shark_number] = prev_list[0][1]
            arr = copy_arr


# 1~ 위 아래 왼 오
time = 0
check = False
while time < 1001:
    marking_gas(arr, k)
    time += 1
    move_shark(arr, n)
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 냄새 1씩 제거
            if gas[i][j][1] != 0:
                gas[i][j][1] -= 1
                if gas[i][j][1] == 0:
                    gas[i][j] = (0, 0)
            # 상어수 체크
            if arr[i][j] != 0:
                cnt += 1
    # 상어가 1만 남은 경우
    if cnt == 1:
        check = True
        break
print(arr)
if check:
    print(time)
else:
    print(-1)
