# 탑 두개 -> 높이 같아야함 (각 탑은 적어도 한개의 블록 포함)
# 모든 블록 사용할 필요없음
# 탑 높이 최대?
# N -> 1 <= 조각 개수 <= 50
# 1 <= 각 조각 높이 <= 500000
# 모든 조각의 높이 합 <= 500000
# https://junh0.tistory.com/2

N = int(input())
heights = [0] + list(map(int, input().split()))
dp = [[-1]*250001 for _ in range(N+1)]
# 블럭 개수
for i in range(1, N+1):
    # 탑 높이 차이
    # 0 생략됨
    for j in range(len(dp[0])):
        # 유지
        dp[i][j] = dp[i-1][j]

        # 차이가 주어진 블럭 높이보다 크거나 같은 경우
        if j - heights[i] >= 0 and dp[i-1][j-heights[i]] != -1:
            dp[i][j] = max(d[i][j], d[i-1][j-heights[i]] + heights[i])
        if heights[i] - j >= 0 and dp[i-1][heights[i]-j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][heights[i]-j]+j)
        if j+heights[i] <= 250000 and dp[i-1][j+heights[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j+heights[i]])
print(dp[N][0] if dp[N][0] else -1)


# def search(n, diff):
#     if diff > 250000:
#         return -1

#     if N == n:
#         if diff == 0:
#             return 0
#         else:
#             return -1

#     if dp[n][diff] != -1:
#         return dp[n][diff]

#     # 선택 안함
#     dp[n][diff] = search(n+1, diff)

#     # 차이 벌리는 경우
#     dp[n][diff] = max(dp[n][diff], search(n+1, diff+heights[n]))

#     # 차이 좁히는 경우
#     if heights[n] > diff:
#         dp[n][diff] = max(dp[n][diff], diff+search(n+1, heights[n]-diff))
#     else:
#         dp[n][diff] = max(dp[n][diff], heights[n] +
#                           search(n+1, diff-heights[n]))

#     return dp[n][diff]


# answer = search(0, 0)

# print(answer if answer > 0 else -1)
