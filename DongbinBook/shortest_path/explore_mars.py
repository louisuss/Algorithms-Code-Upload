import heapq

t = int(input())

# solution1 - dp
result = []
for _ in range(t):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        field[0][i] = field[0][i] + field[0][i-1]
        field[i][0] = field[i][0] + field[i-1][0]

    for i in range(1, n):
        for j in range(1, n):
            field[i][j] = field[i][j] + min(field[i-1][j], field[i][j-1])
    result.append(field[n-1][n-1])

for res in result:
    print(res)


# solution2 - dijkstra
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    distance = [[INF] * n for _ in range(n)]
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])
