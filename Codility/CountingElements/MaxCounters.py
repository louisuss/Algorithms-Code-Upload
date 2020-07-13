# index 1부터 시작
# A[K] = X, 1<=X<=N
# A[K] = N+1 K-> Max Counter
# Timeout
# 77%
def solution(N, A):
    a = [0]*N
    max_num = 0
    for i in range(len(A)):
        if 0 <= A[i]-1 <= N-1:
            a[A[i]-1] += 1
            max_num = max(max_num, a[A[i]-1])
        else:
            a = [max_num]*N
    return a

# 66%


# def solution(N, A):
#     a = [0 for _ in range(N)]
#     max_num = 0
#     for i in range(len(A)):
#         if 0 <= A[i]-1 <= N-1:
#             a[A[i]-1] += 1
#             max_num = max(max_num, a[A[i]-1])
#         else:
#             a = [max_num for _ in range(N)]
#     return a
