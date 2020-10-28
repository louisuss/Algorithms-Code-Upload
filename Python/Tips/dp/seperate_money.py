n, m = map(int, input().split())
# 화폐 단위 정보
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [float('inf')]*(m+1)

dp[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        # 화폐단위2 인 경우 -> dp[2], dp[4], dp[6] ...
        if dp[j-arr[i]] != float('inf'):
            # 현재 dp 값과 현재 화폐단위 전의 dp 값에 현재단위 화폐를 추가한 경우 중 작은 값
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

if dp[m] == float('inf'):
    print(-1)
else:
    print(dp(m))
