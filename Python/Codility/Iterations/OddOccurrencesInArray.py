from functools import reduce


def solution(A):
    return reduce(lambda x, y: x ^ y, A)

# from collections import Counter
# def solution(A):
#     cnt = 0
#     A.sort()
#     if len(A) == 1:
#         return A[0]
#     else:
#         for i in range(len(A)-1):
#             if A[i] == A[i+1]:
#                 cnt += 1
#             else:
#                 cnt += 1
#                 if cnt % 2 != 0:
#                     return A[i]


# def solution(A):

#     if len(A) == 1:
#         return A[0]

#     A.sort()
#     for i in range(0, len(A), 2):
#         if i+1 == len(A):
#             return A[i]
#         if A[i] != A[i+1]:
#             return A[i]


# def solution(A):
#     A = Counter(A)
#     for i in A.items():
#         if i[1] == 1:
#             return i[0]
#     return 0
