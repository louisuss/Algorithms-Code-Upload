# 이분 매칭되는 경우에서 최대 비용 간선 찾기
# https://github.com/jovialcode/algorithm/blob/master/baekjoon/1348.cpp

from collections import deque

R, C = map(int, input().split())
carpark = [list(input()) for _ in range(R)]
car_num, parking_num = 0, 0
cars, parking, walls = {}, {}, []
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for i in range(R):
    for j in range(C):
        if carpark[i][j] == 'C':
            car_num += 1
            cars[car_num] = (i, j)
        if carpark[i][j] == 'P':
            parking_num += 1
            parking[parking_num] = (i, j)
        if carpark[i][j] == 'X':
            walls.append((i, j))

# 인덱스 11 부터 시작 - 차와 주차장 별 거리
distances = [[0]*(car_num+1) for _ in range(parking_num+1)]

# 차가 주차장 까지 갈수 있으면 return 거리 아니면 -1


def cal_distance(a, b):
    start_y, start_x = cars[a]
    end_y, end_x = parking[b]

    visited = [[0]*C for _ in range(R)]
    distance = 0

    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = 0

    while q:
        v_y, v_x = q.popleft()

        if v_y == end_y and v_x == end_x:
            return visited[v_y][v_x]

        # 이동하는 경우
        for dy, dx in dirs:
            ny, nx = dy+v_y, dx+v_x
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and carpark[ny][nx] != 'X':
                    visited[ny][nx] = visited[v_y][v_x] + 1
                    q.append((ny, nx))
    return -1


def dfs(cur):
    visited[cur] = True


def min_time(d):
    visited = [False]*(R+1)
    for i in range(1, C+1):


def solution():
    if car_num > parking_num:
        return -1

    if car_num == 0:
        return 0

    # 비용 계산
    for i in range(1, car_num+1):
        for j in range(1, parking_num+1):
            distances[i][j] = cal_distance(i, j)

    return min_time(distances)


print(solution())
