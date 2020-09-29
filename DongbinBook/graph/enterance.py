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


# 탑승구 개수
g = int(input())
# 비행기 개수
p = int(input())
# 부모 테이블 초기화
parent = [0]*(g+1)

for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))  # 현재 비행기의 탑승구의 부모 확인
    # 부모가 0이면 종료
    if data == 0:
        break
    # 부모가 0이 아니면 현재 탑승구 왼쪽과 합치기
    union_parent(parent, data, data-1)
    result += 1

print(result)
