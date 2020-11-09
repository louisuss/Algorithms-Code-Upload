n, s, m = map(int, input().split())
vol_gap = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1  # 시작 볼륨 초기화

# 곡수 - 행
for i in range(1, n+1):
    # 볼륨 - 열 (0~m)
    for j in range(m+1):
        if dp[i-1][j] == 0:
            continue
        if j - vol_gap[i-1] >= 0:
            dp[i][j-vol_gap[i-1]] = 1
        if j + vol_gap[i-1] <= m:
            dp[i][j+vol_gap[i-1]] = 1

result = -1
# 역순 출력
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)


# 메모리 초과
dp = [[] for _ in range(n)]

if s + vol_gap[0] <= m:
    dp[0].append(s+vol_gap[0])
if s - vol_gap[0] >= 0:
    dp[0].append(s-vol_gap[0])

check = True
for i in range(1, n):
    if dp[i-1]:
        for val in dp[i-1]:
            if val + vol_gap[i] <= m:
                dp[i].append(val+vol_gap[i])
            if val - vol_gap[i] >= 0:
                dp[i].append(val-vol_gap[i])
    else:
        check = False
        break
if check:
    print(max(dp[n-1]))
else:
    print(-1)
