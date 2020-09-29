# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

n, m = map(int, input().split())

total_cost = 0  # 총 설치 비용
cases = []
for _ in range(m):
    a, b, c = map(int, input().split())
    total_cost += c
    cases.append((c, a, b))

parent = [0] * m
# 부모 초기화
for i in range(m):
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


cases.sort()  # 비용 작은 순으로 정렬

min_cost = 0
for case in cases:
    cost, a, b = case
    # 싸이클 발생하지 않는 경우
    if find_parent(parent, a) != find_parent(parent, b):
        min_cost += cost  # 최소비용 추가
        union_parent(parent, a, b)  # 합치기
result = total_cost - min_cost

print(result)
