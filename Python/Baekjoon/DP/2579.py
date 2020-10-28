n = int(input())
s = [0] * 301
dp = [0] * 301

for i in range(n):
    s[i] = int(input())

# 첫번째 계단
dp[0] = s[0]
# 두번째 계단
dp[1] = s[0] + s[1]
# 세번째 계단
dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(3, n):
    # 계단마다 최대 dp 값을 구함
    # 전칸에서 올라온 경우 / 전전칸에서 올라온 경우
    dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
print(dp[n-1])