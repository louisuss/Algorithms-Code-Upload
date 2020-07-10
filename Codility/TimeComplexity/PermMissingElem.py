def solution(A):
    return sum(range(1, len(A)+2)) - sum(A)


# def solution(A):
#     answer = -1
#     A.sort()
#     for i in range(1, len(A)+1):
#         if A[i-1] != i:
#             answer = i
#             break
#     return answer


# def solution(A):
#     answer = 0
#     for i, v in enumerate(sorted(A)):
#         if (i+1) != v:
#             answer = i+1
#             break
#     return answer


# def solution(A):
#     if len(A) == 1 and A[0] != 1:
#         return 1
#     if len(A) == 1 and A[0] == 1:
#         return 2

#     for a, b in zip(sorted(A), list(range(1, len(A)+1))):
#         if a != b:
#             return b
