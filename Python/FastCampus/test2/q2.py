# 가장 긴 내림차순
n = int(input())
soldiers = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(dp)
print(n - max(dp))