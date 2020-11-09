from collections import deque

# n**2


def bfs(x, y):
    q = deque([(x, y)])
    field[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                if not field[nx][ny]:
                    # 처음에 그냥 += 1 해버림. 이동횟수가 누적되야 하므로 이전값 + 1 해야함.
                    field[nx][ny] = field[x][y] + 1
                    q.append((nx, ny))


n, m = map(int, input().split())
x, y = map(int, input().split())

field = [[-1]*(n+1) for _ in range(n+1)]
enemies = []
for _ in range(m):
    a, b = map(int, input().split())
    # field[a][b] = 1
    enemies.append((a, b))

dx = (-2, -2, -1, -1, 1, 1, 2, 2)
dy = (-1, 1, -2, 2, -2, 2, -1, 1)

bfs(x, y)
result = []
for enemy in enemies:
    a, b = enemy
    result.append(field[a][b])

for res in result:
    print(res, end=" ")
