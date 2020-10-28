# O(n)
def solution(X, A):
    # 1~X
    nums = [0]*(X+1)
    cnt = 0
    for i in range(len(A)):
        if nums[A[i]] == 0:
            nums[A[i]] = 1
            cnt += 1
        if cnt == X:
            return i
    return -1

# O(n**2)
# def solution(X, A):
#     nums = [i for i in range(1, X+1)]
#     for i, v in enumerate(A):
#         if v in nums:
#             nums.remove(v)
#         if nums == []:
#             return i
#     return -1
