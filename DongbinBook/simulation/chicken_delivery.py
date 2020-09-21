# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1

from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
town = []
chicken_lst = []
house_lst = []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house_lst.append((r, c))
        if data[c] == 2:
            chicken_lst.append((r, c))

# r_len = n
# c_len = len(town[0])

# Solution 1

# 모든 조합
cases = list(combinations(chicken_lst, m))

# 치킨 거리 합 계산


def get_sum(case):
    result = 0
    # 모든 집에 대해 치킨집별 최단 거리
    for hr, hc in house_lst:
        temp = int(1e9)
        # 치킨집 위치
        for cr, cc in case:
            temp = min(temp, abs(hr-cr)+abs(hc-cc))
        result += temp
    return result


result = int(1e9)
for case in cases:
    result = min(result, get_sum(case))
print(result)

# # Solution 2 - BF
# result = int(1e9)
# house_len = len(house_lst)
# for chicken_case in combinations(chicken_lst, m):
#     visited = [[False]*c_len for _ in range(r_len)]

#     distance = 1
#     temp_res = 0
#     house_cnt = 0
#     while True:
#         # 거리를 1씩 늘려가며 치킨집에서 거리를 만족하는 집 찾기
#         for ck in chicken_case:
#             for house in house_lst:
#                 # 해당 거리에 해당하고 방문안한 경우
#                 if abs(ck[0]-house[0]) + abs(ck[1]-house[1]) == distance and not visited[house[0]][house[1]]:
#                     # 방문 체크
#                     visited[house[0]][house[1]] = True
#                     # 방문가능 집 개수 추가
#                     house_cnt += 1
#                     # 총 거리 추가
#                     temp_res += distance
#                 # 집 모두 방문한 경우 종료
#         if house_cnt == house_len:
#             break

#         # 거리 늘려 다시 진행
#         distance += 1
#     result = min(result, temp_res)
# print(result)

# Solution3 - BFS -> 지난길을 계속 지나게 됨...
# 방문처리를 해서 중복을 없애는 경우 그길을 다른 경우가 이용못하게됨.
# house_len = len(house_lst)
# dirs = [(0,1), (1,0), (0,-1), (-1,0)]
# def bfs(case, r_len, c_len):
#     print(case)
#     field = deepcopy(town)
#     q = deque(case)
#     visited = [[False]*c_len for _ in range(r_len)]

#     result = 0
#     cnt = 0
#     distance = 1
#     while q:
#         new_q = deque()
#         r, c = q.popleft()
#         visited[r][c] = True

#         for dr, dc in dirs:
#             nr, nc = r+dr, c+dc
#             if 0 <= nr < r_len and 0 <= nc < c_len:
#                 # 해당 거리에 맞는 집을 찾은 경우
#                 if field[nr][nc] == 1:
#                     cnt += 1
#                     result += distance
#                     field[nr][nc] = 0
#                 if not visited[nr][nc]:
#                     new_q.append((nr, nc))
#                 visited[nr][nc] = True

#         if cnt == house_len:
#             return result
#         distance += 1
#         q = new_q

#     return 1000

# result = int(1e9)
# for chicken_case in combinations(chicken_lst, m):
#     result = min(result, bfs(chicken_case, r_len, c_len))
# print(result)
