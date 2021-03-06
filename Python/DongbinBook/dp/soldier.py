n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

# 가장 긴 증가하는 부분수열
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
