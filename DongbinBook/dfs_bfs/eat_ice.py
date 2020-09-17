n, m = map(int, input().split())
ice_board = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def dfs(row, col):
    visited[row][col] = 1

    for dir in dirs:
        r, c = dir
        nr, nc = row + r, col + c
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc] and ice_board[nr][nc] == 0:
                dfs(nr, nc)

count = 0
for i in range(n):
    for j in range(m):
        if ice_board[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)

# n, m = map(int, input().split())
# board = [list(map(int, list(input()))) for _ in range(n)]
# dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# def dfs(r, c):
#     board[r][c] = 1
#     for dr, dc in dirs:
#         nr, nc = dr+r, dc+c
#         if 0 <= nr < n and 0 <= nc < m:
#             if not board[nr][nc]:
#                 dfs(nr, nc)


# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if not board[i][j]:
#             dfs(i, j)
#             cnt += 1

# print(cnt)
# print(board)
