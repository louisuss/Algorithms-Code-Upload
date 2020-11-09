from collections import deque


def bfs(viruses):
    q = deque(viruses)

    while q:
        number, time, x, y = q.popleft()
        # time 위치 혼동. 처음에 for 문 밑에 뒀었음. 하지만 그런 경우 time+1 = s 가 먼저 된경우 뒤에 값에 대해 처리를 못함
        if time == s:
            return
        time += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                if not field[nx][ny]:
                    field[nx][ny] = number
                    q.append((number, time, nx, ny))


n, k = map(int, input().split())
field = [[] for _ in range(n+1)]
for i in range(1, n+1):
    field[i].extend([0] + list(map(int, input().split())))

viruses = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if field[i][j] != 0:
            viruses.append((field[i][j], 0, i, j))
viruses.sort()

s, x, y = map(int, input().split())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

bfs(viruses)
print(field[x][y])
