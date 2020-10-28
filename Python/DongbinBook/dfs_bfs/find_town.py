from collections import deque

# 도시수, 도로수, 거리 정보, 출발도시
n, m, k, x = map(int, input().split())
maps = [[] for _ in range(m+1)]

for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
result = []
while q:
    now = q.popleft()
    for next_pos in maps[now]:
        if distance[next_pos] == -1:
            distance[next_pos] = distance[now] + 1
            if distance[next_pos] == k:
                result.append(next_pos)
            q.append(next_pos)

if result:
    for res in result:
        print(res)
else:
    print(-1)

