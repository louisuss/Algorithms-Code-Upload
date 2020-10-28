def solution(m, n, puddles):
    answer = [[0]*(m+1) for _ in range(n+1)]
    answer[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                answer[i][j] = 0
            else:
                answer[i][j] = answer[i-1][j] + answer[i][j-1]
    return answer[n][m] % 1000000007

# m 열 n 행
# (1,1) (m,n)


# def solution(m, n, puddles):
#     dp = [[0]*(m+1) for _ in range(n+1)]
#     # 웅덩이 체크 -> -1
#     for x, y in puddles:
#         dp[y][x] = -1

#     # 세로줄 채우기
#     for y in range(1, n+1):
#         # 이전 값이 웅덩이이면 종료
#         if dp[y-1][1] == -1:
#             break
#         else:
#             dp[y][1] = 1
#     # 가로줄 채우기
#     for x in range(1, m+1):
#         if dp[1][x-1] == -1:
#             break
#         else:
#             dp[1][x] = 1

#     for i in range(2, n+1):
#         for j in range(2, m+1):
#             if dp[i][j] == -1:
#                 continue
#             # 둘다 우물이 아닌 경우
#             if dp[i-1][j] != -1 and dp[i][j-1] != -1:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#             elif dp[i-1][j] == -1 and dp[i][j-1] != -1:
#                 dp[i][j] += dp[i][j-1]
#             elif dp[i-1][j] != -1 and dp[i][j-1] == -1:
#                 dp[i][j] += dp[i-1][j]
#             elif dp[i-1][j] == -1 and dp[i][j-1] == 1:
#                 break

#     return dp[n][m] % 1000000007
