n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

dp = [10001] * (m+1)
dp[0] = 0
for mon in money:
    for i in range(mon, m+1):
        if dp[i-mon] != 10001:
            d[i] = min(dp[i], dp[i-mon]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
