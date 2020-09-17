# 백준 14502
# 삼성전자 SW 기출

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

from itertools import combinations
from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(start):
    stack = [start]

    while stack:
        virus = stack.pop()
        for r, c in dirs:
            nr, nc = virus[0] + r, virus[1] + c
            if 0 <= nr < n and 0 <= nc < m:
                if copy_field[nr][nc] == 0:
                    copy_field[nr][nc] = 2
                    stack.append((nr, nc))

    # for r, c in dirs:
    #     nr, nc = start[0] + r, start[1] + c
    #     if 0 <= nr < n and 0 <= nc < m:
    #         if copy_field[nr][nc] == 0:
    #             copy_field[nr][nc] = 2
    #             dfs((nr, nc))


def bfs(start):
    q = deque([start])

    while q:
        virus = q.popleft()
        for r, c in dirs:
            nr, nc = virus[0] + r, virus[1] + c
            if 0 <= nr < n and 0 <= nc < m:
                if copy_field[nr][nc] == 0:
                    copy_field[nr][nc] = 2
                    q.append((nr, nc))


zero_lst = []
virus_lst = []
for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            zero_lst.append((i, j))
        if field[i][j] == 2:
            virus_lst.append((i, j))

result = 0
for case in combinations(zero_lst, 3):
    copy_field = deepcopy(field)
    a, b, c = case

    # 벽 배치
    copy_field[a[0]][a[1]], copy_field[b[0]
                                       ][b[1]], copy_field[c[0]][c[1]] = 1, 1, 1

    # # 바이러스 퍼뜨리기
    for virus in virus_lst:
        dfs(virus)

    # 0 인 부분 개수 출력
    cnt = 0
    for cf in copy_field:
        cnt += cf.count(0)

    # 최대값 체크
    result = max(result, cnt)
print(result)
