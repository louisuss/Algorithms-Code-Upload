# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

n = int(input())
time = [] # 걸리는 시간
money = [] # 버는 금액
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)

for i in range(n-1, -1, -1):
    # i -> 현재 기간 
    t = time[i] + i # 필요한 기간 + 현재 기간
    # 상담 기간 조건 맞는 경우
    if t <= n:
        # dp[t] -> 그 기간에 최대 금액
        dp[i] = max(money[i] + dp[t], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어난 경우
    else:
        dp[i] = max_value
    print(dp)
print(max_value)

