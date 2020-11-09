n = int(input())
a = list(map(int, input().split()))

dp = [1]*n # 최소1개로 초기화
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
