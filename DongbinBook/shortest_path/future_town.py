# Test Case
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

INF = int(1e9)
# 회사수, 경로수
n, m = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
# 목적지, 소개팅
x, k = map(int, input().split())
dp = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dp[i][j] = 0
            break

for a, b in routes:
    dp[a][b] = 1
    dp[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

answer = dp[1][k] + dp[k][x]

if answer >= INF:
    print(-1)
else:
    print(answer)
