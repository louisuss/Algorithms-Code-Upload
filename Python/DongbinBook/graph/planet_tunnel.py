# 5
# 11 - 15 - 15
# 14 - 5 - 15
# -1 - 1 - 5
# 10 - 4 - 1
# 19 - 4 19
# Solution1
n = int(input())
INF = int(1e9)
pos = [0]+[list(map(int, input().split())) for _ in range(n)]

planets = [[INF]*(n+1) for _ in range(n+1)]  # 이차원 행렬로 연결상태 표시
costs = []  # 최소비용 구하기 위한 리스트
for i in range(1, n):
    for j in range(i+1, n+1):
        x1, y1, z1 = pos[i]
        x2, y2, z2 = pos[j]
        planets[i][j] = min(abs(x1-x2), abs(y1-y2),
                            abs(z1-z2))  # 각 연결별 최단 거리 구하기
        costs.append((planets[i][j], i, j))

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


costs.sort()
result = 0
for cost in costs:
    c, a, b = cost
    if find_parent(parent, a) != find_parent(parent, b):
        result += c
        union_parent(parent, a, b)

print(result)

# Solution2
n = int(input())
edges = []
result = 0

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n-1):
    # 비용순으로 정렬하기 위해 튜플의 첫 원소를 비용으로 설정
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
    print(edges)
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
