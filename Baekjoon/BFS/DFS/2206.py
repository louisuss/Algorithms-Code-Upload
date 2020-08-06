from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
# d / u /  r / l
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    q = deque()
    q.append((0,0,0))
    dist[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        # finish
        if x == n-1 and y == m-1:
            return dist[x][y][z]

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny][z]:
                continue

            # 이동 가능할 때
            if maps[nx][ny] == 0:
                # 카운팅
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))

            # 벽이 있고 벽을 부술 수 있을 때
            if maps[nx][ny] == 1 and z == 0:
                # 카운팅
                dist[nx][ny][1] = dist[x][y][z] + 1
                q.append((nx, ny, 1))
    return -1
print(bfs())

# q = deque()
# def bfs():
#     q.append([0,0,0])
#     c[0][0][0] = 1
#     while q:
#         x, y, z = q.popleft()
#         for dx, dy in dirs:
#             nx = x + dx
#             ny = y + dy
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if maps[nx][ny] == 0 and c[nx][ny][z] == -1:
#                     c[nx][ny][z] = c[x][y][z] + 1
#                     q.append([nx, ny, z])
#                 elif z == 0 and maps[nx][ny] == 1 and c[nx][ny][z+1] == -1:
#                     c[nx][ny][z+1] = c[x][y][z] + 1
#                     q.append([nx, ny, z+1])
#
# bfs()
# ans1, ans2 = c[n-1][m-1][0], c[n-1][m-1][1]
# if ans1 == -1 and ans2 != -1:
#     print(ans2)
# elif ans1 != -1 and ans2 == -1:
#     print(ans1)
# else:
#     print(min(ans1, ans2))
#
