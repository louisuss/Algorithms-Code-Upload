n = int(input())
m = int(input())
INF = int(1e9)
cost = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = c

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][i] + cost[i][b])

for i in range(len(cost)):
    if i == 0:
        continue
    for j in range(len(cost[i])):
        if j == 0:
            continue
        print(cost[i][j], end=" ")
    print()


# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4
