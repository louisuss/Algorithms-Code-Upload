# 길이 합 최소 구하기

from collections import defaultdict
import math

# 위치간 거리 구하기


def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a*a) + (b*b))

# 부모 위치 구하기


def get_parent(parent, x):
    if parent[x] == x:
        return x
    return get_parent(parent, parent[x])

# 부모 결합


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모가 같은지 여부 확인


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False


edges = []  # 위치들에 대한 모든 위치 조합
parent = {}  # 부모 집합
locations = []  # 위치
n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

# 모든 위치 조합 구하기
len_locations = len(locations)
for i in range(len_locations - 1):
    for j in range(i+1, len_locations):
        # (a, b, 거리)
        edges.append((i+1, j+1, get_distance(locations[i], locations[j])))

# 부모 집합 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 연결된 부분 부모 합치기
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 거리가 짧은 순서로 정렬
edges.sort(key=lambda x: x[2])

result = 0
for a, b, cost in edges:
    # 부모가 같지 않은 경우 -> 사이클 발생, 중복 안되는 경우임. 부모 합치기.
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print("%0.2f" % result)
