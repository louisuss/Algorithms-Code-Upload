

# from math import sqrt
# def prime_list(n):
#     sieve = [True] * n
#     m = int(sqrt(n))
#     for i in range(2, m+1):
#         if sieve[i] == True:
#             for j in range(2*i, n, i):
#                 sieve[j] = False
#     return [i for i in range(2,n) if sieve[i] == True]
#
# def prime_num(n):
#     li = prime_list(n)
#     idx = max([i for i in range(len(li)) if li[i] <= n/2])
#     for i in range(idx, -1, -1):
#         for j in range(i, len(li)):
#             if li[i] + li[j] == n:
#                 return [li[i], li[j]]
# for _ in range(int(input())):
#     n = int(input())
#     print(" ".join(map(str,prime_num(n))))

prime_list = [True for i in range(10001)]

for i in range(2, 10001):
    if prime_list[i]:
        for j in range(2*i, 10001, i):
            prime_list[j] = False
T = int(input())
for _ in range(T):
    n = int(input())
    a = n // 2
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a-=1
            b+=1


# prime_num = [0 for i in range(10001)]
# prime_num[1] = 1
# for i in range(2, 98):
#     for j in range(i*2, 10001, i):
#         prime_num[j] = 1
# t = int(input())
#
# for _ in range(t):
#     a = int(input())
#     b = a // 2
#     for j in range(b, 1, -1):
#         if prime_num[a - j] == 0 and prime_num[j] == 0:
#             print(j, a-j)
#             break


# import math
# T = int(input())
# lis = list()
# for _ in range(T):
#     lis.append(int(input()))
#
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True
#
# for i in lis:
#     lis2 = []
#     for j in range(2, i+1):
#         if is_prime(j):
#             lis2.append(j)
#     for _ in range(len(lis)-1):
#         for l in range(len(lis)-1):




