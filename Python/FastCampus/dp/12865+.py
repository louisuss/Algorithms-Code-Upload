# 모든 무게에 대해 최대 가치 저장하기
# dp[i][j] = 배낭에 넣은 물품의 무게합이 j일 때 얻을 수 있는 최대 가치

n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]  # 가치

# i = 물품 번호
for i in range(1, n+1):
    weight, value = map(int, input().split())
    # 열 (무게 - 추가 가능한 무게)
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 추가 가능한 경우
        else:
            # 현재 무게를 추가하지 않은 이전 가치, 이전까지의(j-weight) 무게 값에 현재 추가되는 가치를 더한값
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
print(dp[n][k])
