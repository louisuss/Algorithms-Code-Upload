# 묘비
# 귀신구멍 - 특정 시간 지난 후 다른 위치 이동 (양, 음, 0)
# 잔디


# 1. 필드에 귀신 구멍(2), 장애물 표시(0), 잔디(1)

# Impossible 출력
# 경로가 벽으로 다 막히거나 (대각선) / 한공간이 귀신 구멍인 경우

# Never 출력
# 과거로 이동의 정의가 모호.. 지난 경로로 이동?
# 귀신구멍으로 이동한곳이 이미 방문한 곳인 경우

import sys
from collections import deque
sys.setrecursionlimit(10**6)


def dfs(x, y, t):
    global go_past
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 현재 지역 방문 체크
    visited[y][x] = True

    # 도착 지점에 도착한 경우
    # -1 빼먹어서 계속 결과 안나왔음....
    if x == (len(ground[0])-1) and (y == len(ground)-1):
        answer.append(t)

    for b, a in dirs:
        # 다음에 이동할 방향
        ny, nx = b + y, a + x

        # 리스트 인덱스 범위 조건 만족하는 경우
        if 0 <= ny < len(ground) and 0 <= nx < len(ground[0]):
            # 방문 안했고 이동가능한 위치인 경우 (장애물:0, 나머지: 상수)
            if not visited[ny][nx] and ground[ny][nx]:
                # 순간이동하는 위치인 경우
                # for문 사용하면 안됨. 이 () in [] 조건 부분에서 에러 - key가 각 (nx, ny)로 전달됨
                if tunnels.get((nx, ny)):
                    # 순간 이동 위치 방문체크
                    visited[ny][nx] = True
                    # 순간이동 위치로 좌표 바꿈
                    cx, cy = tunnels[(nx, ny)][0]
                    # 순간 이동한 위치가 이미 방문된 경우: Never 출력
                    # if visited[cy][cx]:
                    #     go_past = True
                    # else:
                    # 순간이동 걸린 시간 추가
                    t += tunnels[(nx, ny)][1]
                    # 순간이동 위치에서 시작
                    dfs(cx, cy, t)
                # 일반 잔디인 경우
                else:
                    dfs(nx, ny, t+1)


def bfs(w, h):
    q = deque([(0, 0, 0)])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False]*w for _ in range(h)]

    while q:
        x, y, t = q.popleft()
        visited[y][x] = True
        print(y, x)

        if x == (len(ground[0])-1) and y == (len(ground)-1):
            answer.append(t)

        for dx, dy in dirs:
            nx, ny = dx + x, dy + y
            if 0 <= nx < len(ground[0]) and 0 <= ny < len(ground):
                if not visited[ny][nx] and ground[ny][nx]:
                    if tunnels.get((nx, ny)):
                        cx, cy = tunnels[(nx, ny)][0]
                        if visited[cy][cx]:
                            go_past = True
                        else:
                            # 이 부분에서 계속 반복됨
                            q.append((cx, cy, t+(tunnels[(nx, ny)][1])))
                    else:
                        q.append((nx, ny, t+1))


while True:
    go_past = False
    answer = []
    w, h = map(int, input().split())
    ground = [[1]*w for _ in range(h)]
    # visited = [[False]*w for _ in range(h)]
    tunnels = {}

    if w == 0 and h == 0:
        break

    # 장애물인 경우 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        ground[y][x] = 0

    # 순간이동 가능 지점 2
    for _ in range(int(input())):
        x1, y1, x2, y2, t = map(int, input().split())
        tunnels[(x1, y1)] = [(x2, y2), t]
        ground[y1][x1] = 2

    # (0, 0) 시작
    dfs(0, 0, 0)
    # bfs(w, h)
    print(answer)
    if go_past:
        print("Never")
    else:
        if answer:
            print(min(answer))
        else:
            print("Impossible")
