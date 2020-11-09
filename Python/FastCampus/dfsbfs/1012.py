# 재귀횟수 제한 없으면 런타임 에러...
import sys
sys.setrecursionlimit(int(1e9))

t = int(input())

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)


def dfs(r, c):
    if arr[r][c] == 1:
        arr[r][c] = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == 1:
                dfs(nr, nc)


result = []

for _ in range(t):
    m, n, k = map(int, input().split())
    # 가로, 세로, 배추 개수
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        # x, y = 가로, 세로
        a, b = map(int, input().split())
        arr[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            # 배추 찾은 경우 -> 벌레 풀기 1 -> 0으로 만들기 or visited 처리
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    result.append(cnt)

for res in result:
    print(res)
