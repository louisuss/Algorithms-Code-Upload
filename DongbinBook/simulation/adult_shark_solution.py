# 인덱스 혼란스럽지 않게 0 부터 시작으로 통일

n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]  # 상어 번호 - 1 해서 사용해야함

directions = list(map(int, input().split()))

# tuple 형식은 연산 안되므로 리스트 형식으로 정의해야함
smell = [[[0, 0]] * n for _ in range(n)]

# 우선순위 - -1 해줘야함
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))  # 번호가 1부터 시작

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄세 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어 위치에 냄세 표시
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]

def move():
    # 이동 결과 담기 위한 임시 테이블
    new_arr = [[0]*n for _ in range(n)]

    # 각 위치를 하나씩 확인
    for r in range(n):
        for c in range(n):
            # 상어 존재하는 경우
            if arr[r][c] != 0:
                direction = directions[arr[r][c] - 1]  # 현재 상어의 방향
                found = False

                # 냄새가 존재하지 않는 곳 체크
                for idx in range(4):
                    # 우선순위에서 상어 번호에 해당, 상어 방향, 이동방향 -> -1은 dirs index 0 부터 시작하기 때문
                    nr = r + dirs[priorities[arr[r][c]-1]
                                  [direction-1][idx] - 1][0]
                    nc = c + dirs[priorities[arr[r][c]-1]
                                  [direction-1][idx] - 1][1]

                    if 0 <= nr < n and 0 <= nc < n:
                        if smell[nr][nc][1] == 0:  # 냄새 존재 X
                            # 상어 방향 변경
                            directions[arr[r][c] -
                                       1] = priorities[arr[r][c]-1][direction-1][idx]

                            # 상어 이동
                            if new_arr[nr][nc] == 0:
                                new_arr[nr][nc] = arr[r][c]
                            else:
                                # 움직이는 순서에 따라 문제가 발생할 수 있음
                                # 다른 상어가 위치한 경우 - 번호작은 상어가 들어감
                                new_arr[nr][nc] = min(
                                    new_arr[nr][nc], arr[r][c])
                            found = True
                            break

                if found:
                    continue

                # 주변에 모두 냄새가 남아있는 경우, 자신의 냄새 있는 곳으로 이동
                for idx in range(4):
                    nr = r + dirs[priorities[arr[r][c]-1]
                                  [direction-1][idx] - 1][0]
                    nc = c + dirs[priorities[arr[r][c]-1]
                                  [direction-1][idx] - 1][1]

                    if 0 <= nr < n and 0 <= nc < n:
                        if smell[nr][nc][0] == arr[r][c]:
                            # 해당 상어 방향 이동
                            directions[arr[r][c] -
                                       1] = priorities[arr[r][c]-1][direction-1][idx]
                            new_arr[nr][nc] = arr[r][c]
                            break
    return new_arr


time = 0
while True:
    update_smell()
    new_arr = move()
    arr = new_arr
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 26:
        print(-1)
        break
