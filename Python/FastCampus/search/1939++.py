from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)] # 가능한 모든 이동 경로 저장

def bfs(c):
    q = deque([start_factory])
    visited = [False] * (n+1)
    visited[start_factory] = True

    while q:
        a = q.popleft() # 시작
        for b, weight in adj[a]: 
            # 이동한 곳 방문X, 중량이 c 이상인경우 통과 가능
            if not visited[b] and weight >= c:
                visited[b] = True
                q.append(b)

    return visited[arrive_factory] # 목적 공장 도착 여부

min_weight = int(1e9)
max_weight = 1

for _ in range(m):
    a, b, weight = map(int, input().split())
    adj[a].append((b, weight))
    adj[b].append((a, weight))
    min_weight = min(min_weight, weight) # 가장 작은 무게
    max_weight = max(max_weight, weight) # 가장 큰 무게 

# 출발, 도착 공장
start_factory, arrive_factory = map(int, input().split())

result = min_weight
while min_weight <= max_weight:
    mid = (min_weight + max_weight) // 2 # mid = 현재 중량

    # 현재 설정한 중량으로 통과 가능한 경우
    if bfs(mid):
        # 결과 저장
        result = mid
        # 가장 작은 무게 증가
        min_weight = mid+1
    else:
        # 가장 큰 무게 감소
        max_weight = mid - 1
print(result)


# result = [[0]*(n+1) for _ in range(n+1)]
# # 메모리 초과
# for info in infos:
#     a, b, c = info
#     if result[a][b] < c:
#         result[a][b] = c
#     if result[b][a] < c:
#         result[b][a] = c

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             result[a][b] = max(result[a][b], min(result[a][k],result[k][b]))
#             result[b][a] = max(result[b][a], min(result[b][k], result[k][a]))

# print(result[factory[0]][factory[1]])

