# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

INF = int(1e9)
n, m = map(int, input().split())
INF = int(1e9)
scores = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    scores[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    scores[a][b] = 1

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            scores[a][b] = min(scores[a][b], scores[a][i] + scores[i][b])

result = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if scores[i][j] != INF or scores[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)
