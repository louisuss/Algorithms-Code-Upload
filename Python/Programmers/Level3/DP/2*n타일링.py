# 나누기 과정을 for문 안에서 미리 처리하니까 효율성 통과

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n] % 1000000007


# # 규칙 찾기
# # 시간초과
# def solution(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     dp = [0]*(n+1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]

#     return dp[n] % 1000000007
