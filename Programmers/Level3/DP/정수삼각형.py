# 인덱스 범위 맞추는게 항상 헷갈린다..
# 인덱스 끝에 맞춰서 -1 방식이 마지막 인덱스 -1 경우 보다 인덱스 범위 맞추기 쉬운것같다.

def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0].append(triangle[0][0])

    # i = 다음 dp / i-1 = 이전 dp
    for i in range(1, len(triangle)):
        # 다음 dp의 범위
        for j in range(i+1):
            # 맨 왼쪽끼리 더하기
            if j == 0:
                dp[i].append(dp[i-1][0] + triangle[i][j])
            # 맨 오른쪽끼리 더하기
            elif j == i:
                dp[i].append(dp[i-1][-1] + triangle[i][j])
            # 중간은 이전 dp 두값비교해야함
            else:
                dp[i].append(max(dp[i-1][j-1]+triangle[i]
                                 [j], dp[i-1][j]+triangle[i][j]))
    return max(dp[len(triangle)-1])


# def solution(triangle):
#     dp = []
#     for t in range(1, len(triangle)):
#         for i in range(t+1):
#             if i == 0:
#                 triangle[t][0] += triangle[t-1][0]
#             elif i == t:
#                 triangle[t][-1] += triangle[t-1][-1]
#             else:
#                 triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
#     return max(triangle[-1])


# solution = lambda t, l = []: max(l) if not t else solution(
#     t[1:], [max(x, y)+z for x, y, z in zip([0]+l, l+[0], t[0])])
