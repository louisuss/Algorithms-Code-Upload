n, m = map(int, input().split())
cities = [[0]*(n+1)]

for _ in range(n):
    temp = [0]+list(map(int, input().split()))
    cities.append(temp)

city_lst = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if j > i and cities[i][j] == 1:
            city_lst.append((i, j))

plans = list(map(int, input().split()))
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


for city in city_lst:
    a, b = city
    union_parent(parent, a, b)

check = True
for idx in range(1, len(plans)):
    if parent[idx] != parent[idx+1]:
        check = False

if check:
    print("YES")
else:
    print("NO")
