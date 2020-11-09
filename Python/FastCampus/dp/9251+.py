x = input()
y = input()

# 두 문자열의 길이를 조금씩 늘려가며 확이하여,  공통 부분 수열의 최대 길이를 계산
dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]
for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
        # 값이 같을 때는 대각선 + 1
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 아닌 경우 위, 왼쪽에서 더 큰값 넣기
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[len(x)][len(y)])
