# def solution(arr):
#     cnt = 2
#     while True:
#         cnt += 1
#         ck = 0
#         for i in arr:
#             if cnt%i == 0 and cnt//i >=1:
#                 ck += 1
#         if ck == len(arr):
#             break
#     return cnt
from math import gcd


def solution(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, int(answer))
    return answer
