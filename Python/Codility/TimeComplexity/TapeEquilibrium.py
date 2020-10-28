def solution(A):
    left_sum = A[0]
    right_sum = sum(A[1:])
    min_diff = abs(left_sum - right_sum)
    for i in range(1, len(A)-1):
        left_sum += A[i]
        right_sum -= A[i]
        min_diff = min(min_diff, abs(left_sum - right_sum))
    return min_diff

# 시간 초과

# def solution(A):
#     answer = 100000
#     for p in range(1, len(A)):
#         answer = min(answer, abs(sum(A[:p]) - sum(A[p:])))
#     return answer
