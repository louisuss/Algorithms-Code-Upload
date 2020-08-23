N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp1 = [[-float('inf')] * (M+1) for _ in range(N)]
dp2 = [[-float('inf')] * (M+1) for _ in range(N)]

dp1[0][0] = 0
dp2[0][1] = arr[0]

# 1~5
for i in range(1, N):
    dp1[i][0] = 0
    dp2[i][0] = -float('inf')
    # 1 ~ min(2, ((1~5)+2) // 2) + 1 -> 1~2 까지만 나오게됨
    for j in range(1, min(M, (i+2)//2)+1):
        print(i, j)
        print()
        # 이전 dp1, dp2 중 큰 값이 다음 dp1
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        # 이전 dp1 + 다음 값, 이전 dp2 + 다 값 중 큰 값이 다음 dp2
        dp2[i][j] = max(dp1[i-1][j-1]+arr[i], dp2[i-1][j] + arr[i])

# [[0, -inf, -inf], [0, -1, -inf], [0, 3, -inf], [0, 4, 0], [0, 6, 5], [0, 10, 9]]
# [[-inf, -1, -inf], [-inf, 3, -inf], [-inf, 4, 0],[-inf, 6, 5], [-inf, 10, 9], [-inf, 9, 8]]
# print(dp1)
# print(dp2)

print(max(dp1[N-1][M], dp2[N-1][M]))
