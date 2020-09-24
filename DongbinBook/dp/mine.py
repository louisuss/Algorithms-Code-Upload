t = int(input())

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# Solution 1 - 리스트 범위를 확장해서 해결
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    mine = [[0]*m for _ in range(n+2)]
    dp = [[0]*m for _ in range(n+2)]

    # 리스트로 변경
    idx = 0
    for i in range(1, n+1):
        for j in range(m):
            mine[i][j] = arr[idx]
            idx += 1

    # dp 초기값 설정
    for i in range(1, n+1):
        dp[i][0] = mine[i][0]

    for col in range(1, m):
        for row in range(1, n+1):
            dp[row][col] = mine[row][col] + \
                max(dp[row-1][col-1], dp[row][col-1], dp[row+1][col-1])
    max_value = 0
    for i in range(1, n+1):
        max_value = max(dp[i][m-1], max_value)
    print(max_value)


# Solution2 - 범위 나가는 조건을 if문을 통해 제약
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    idx = 0
    for i in range(n):
        dp.append(arr[idx:idx+m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            # 범위 나가는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
