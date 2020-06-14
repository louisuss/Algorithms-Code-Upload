import sys
sys.setrecursionlimit(10000)

t = int(input())
b, ck = [], []

# Flood Fill
# 전체 탐색하고 탐색한 곳을 다시 탐색하지 않는 것이 핵심
dx, dy = [1,0,-1,0], [0,1,0,-1]
def dfs(x, y):
    global b, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if b[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx, yy)

def process():
    global b, ck
    m, n, k = map(int, input().split())
    # 배열 크기를 1씩 증가 시킴
    b = [[0 for i in range(m+2)] for _ in range(n+2)]
    ck = [[0 for i in range(m+2)] for _ in range(n+2)]
    for _ in range(k):
        x, y = map(int, input().split())
        b[y+1][x+1] = 1

    ans = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            if b[i][j] == 0 or ck[i][j]:
                continue
            dfs(i,j)
            ans += 1
    print(ans)


for _ in range(t):
    process()

# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(x, y):
#     visited[x][y] = True
#     directions = [(-1,0),(1,0),(0,-1),(0,1)]
#     for dx, dy in directions:
#         nx, ny = x+dx, y+dy
#         if nx < 0 or nx >= n or ny < 0 or ny >= m:
#             continue
#         if arr[nx][ny] and not visited[nx][ny]:
#             dfs(nx, ny)
#
# for _ in range(int(input())):
#     m, n, k = map(int, input().split())
#     arr = [[0] * m for _ in range(n)]
#     visited = [[False]*m for _ in range(n)]
#     for _ in range(k):
#         y, x = map(int, input().split()) # col row
#         arr[x][y] = 1
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] and not visited[i][j]:
#                 dfs(i,j)
#                 result += 1
#     print(result)

# t = int(input())
# for _ in range(t):
#     M, N, K = map(int, input().split())
#     adj = [[] for _ in range(N+1)]
#
#     for _ in range(K):
#         x, y = map(int, input().split())
#         adj[x].append(y)
#         adj[y].append(x)
#
# def dfs()

