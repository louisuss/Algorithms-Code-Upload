n = int(input())
apt_map = []

def dfs(cnt, x, y):
    visited[x][y] = True
    directions = [(-1,0), (1, 0), (0,1), (0,-1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if apt_map[nx][ny] and not visited[nx][ny]:
            cnt = dfs(cnt+1, nx, ny)
    return cnt



for _ in range(n):
    x = ' '.join(input())
    apt_map.append(list(map(int, x.split())))

ans = []
result = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if apt_map[i][j] == 1 and not visited[i][j]:
            ans.append(dfs(1, i, j))
print(len(ans))
for i in sorted(ans):
    print(i)

