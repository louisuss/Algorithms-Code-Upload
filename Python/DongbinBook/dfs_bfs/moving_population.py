from collections import deque
from copy import deepcopy

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

result = 0

def process(x, y, index):
    # 연합
    united = []
    united.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index # 연합 번호등록
    summary = countries[x][y] # 총 인구수
    cnt = 1 # 연합 국가수

    while q:
        x, y = q.popleft()
        for dir in dirs:
            nx, ny = x+dir[0], y+dir[1]
            # 범위 조건 만족, 연합번호가 없는 경우
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 인구차가 범위안에 있는 경우
                if l <= abs(countries[nx][ny] - countries[x][y]) <= r:
                    # 인접 국가 찾기
                    q.append((nx, ny))
                    # 연합 등록
                    union[nx][ny] = index
                    # 인구수 추가
                    summary += countries[nx][ny]
                    # 연합 국가 추가
                    cnt += 1
                    united.append((nx, ny))

    for i, j in united:
        countries[i][j] = summary // cnt

# 합쳐지는 횟수
total_cnt = 0
while True:
    # 연합 번호 등록위한 리스트
    union = [[-1]*n for _ in range(n)]
    # 연합 번호
    index = 0
    for i in range(n):
        for j in range(n):
            # 연합이 없는 나라
            if union[i][j] == -1:
                # 연합 만들기
                process(i, j, index)
                # ++연합번호 
                index += 1
    # 연합의 개수가 리스트의 개수인 경우 - 더이상 합칠 수 없는 경우
    if index == n*n:
        break
    # 합쳐지는 횟수 증가
    total_cnt += 1

print(total_cnt)


# Solution2 - visited 부분이 추가가 안됨
# def bfs(i, j, left, right):
#     united = [(i, j)]
#     q = deque([(i,j)])
#     visited[i][j] = True
#     cnt = 1
#     sum_value = countries[i][j]

#     while q:
#         x, y = q.popleft()

#         for dx, dy in dirs:
#             nx, ny = dx + x, dy + y
#             # 리스트 범위 안에 있는 것
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 # 방문 안했고 인구차이 조건 만족하는 경우
#                 if (left <= abs(countries[nx][ny] - countries[x][y]) <= right):
#                     # 다음 진행을 위해 저장
#                     q.append((nx, ny))
#                     visited[nx][ny] = True
#                     sum_value += countries[nx][ny]
#                     cnt += 1
#                     # 지나간 경로 저장
#                     united.append((nx, ny))
#     for i, j in united:
#         countries[i][j] = sum_value // cnt

#     if united:
#         return 1
#     else:
#         return 0
    
# answer = 0
# total = 0
# while True:
#     answer = 0
#     visited = [[False]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             answer += bfs(i, j, l, r)
    
#     if not answer:
#         break
#     total += 1

# print(total)
    
