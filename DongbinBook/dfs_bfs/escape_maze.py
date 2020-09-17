from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 1


def bfs(row, col):
    global count
    q = deque([(row, col)])
    visited[row][col] = 1

    while q:
        row, col = q.popleft()
        if row == n-1 and col == m-1:
            return visited[row][col]

        for dir in dirs:
            r, c = dir
            nr, nc = row + r, col + c
            if 0 <= nr < n and 0 <= nc < m:
                if maze[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = visited[row][col] + 1
                    q.append((nr, nc))


print(bfs(0, 0))
