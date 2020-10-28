# from itertools import permutations
#
#
# def solution(numbers):
#     answer = 0
#     numbers = list(numbers)
#     n = len(numbers)
#
#     nums = []
#     for i in range(1, n + 1):
#         temp = permutations(numbers, i)
#         for j in temp:
#             nums.append(int(''.join(j)))
#     nums = set(nums)
#     max_val = max(nums)
#
#     li = [True] * (max_val + 1)
#     li[0], li[1] = False, False
#
#     m = int(max_val ** 0.5)
#     for i in range(2, m + 1):
#         if li[i]:
#             for j in range(2 * i, max_val + 1, i):
#                 li[j] = False
#
#     for i in nums:
#         if li[i]:
#             answer += 1
#     return answer

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map(''.join, permutations(list(n), i+1))))

    a -= set(range(0,2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i*2, max(a) + 1,i))

    return len(a)