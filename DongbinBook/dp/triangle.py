# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

n = int(input())
dp = [[0]]
for _ in range(n):
    temp = list(map(int, input().split()))
    dp.append(temp)

for i in range(2, n+1):
    for j in range(i):
        if j == 0:
            dp[i][0] = dp[i][0] + dp[i-1][0]
        elif j == i-1:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n]))
