import math

def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i):
        print(i)

# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     cnt = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             cnt += 1
#             if cnt >= 3:
#                 break
#     if cnt == 2:
#         print(i)