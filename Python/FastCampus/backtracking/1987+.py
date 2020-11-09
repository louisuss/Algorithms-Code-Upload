from collections import deque
import sys
sys.setrecursionlimit(int(1e9))


def bfs(x, y):
    global result
    # 리스트 사용 시 시간 초과
    q = set()  # 중복 방문 제거
    q.add((x, y, field[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # step에 이전 경로 기록되기 때문에 방문했던 곳 다시 이동 안함
            if 0 <= nx < r and 0 <= ny < c and field[nx][ny] not in step:
                q.add((nx, ny, step + field[nx][ny]))  # 경로 기록

# 에러 - visited 사용 시 방문 경로에 따라 정답이 바뀜
# def bfs2(x, y):
#     global result
#     # 리스트 사용 시 시간 초과
#     q = deque([])
#     q.append((x, y, field[x][y]))

#     while q:
#         x, y, step = q.popleft()
#         result = max(result, len(step))
#         visited[x][y] = True
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # step에 이전 경로 기록되기 때문에 방문했던 곳 다시 이동 안함
#             if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and field[nx][ny] not in step:
#                 visited[nx][ny] = True
#                 q.append((nx, ny, step + field[nx][ny]))  # 경로 기록

# 메모리 초과


def dfs(x, y, temp):
    global result
    temp += field[x][y]
    result = max(result, len(temp))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 중복되는 알파벳 조건때문에 방문한곳 다시 방문안함
        if 0 <= nx < r and 0 <= ny < c and field[nx][ny] not in temp:
            dfs(nx, ny, temp)


r, c = map(int, input().split())
field = [list(input()) for _ in range(r)]
# CBAB
# ADCB
# CBD
# visited = [[False]*c for _ in range(r)] # visited 사용 시 이미 처리한 경우 먼저 처리한 경우에 따라 정답이 바뀜

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
# bfs(0, 0)
dfs(0, 0, "")
print(result)


# RecursionError: maximum recursion depth exceeded in comparison
# def dfs(passed, x, y):
#     global result

#     passed.append(field[x][y])
#     visited[x][y] = True

#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#         if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
#             if field[nx][ny] not in passed:
#                 dfs(passed, nx, ny)
#             else:
#                 passed.pop()
#                 result = max(result, len(passed))

# dfs([], 0, 0)
# print(result)
