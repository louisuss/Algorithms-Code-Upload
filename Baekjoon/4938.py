N = 123456 * 2 + 1
sieve = [True] * N

for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 +1):
        if sieve[i]:
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)
    
# import sys
# import math
#
# limit = 123456
#
# eratos = [1]*(2*limit+1)
# eratos[0] = 0
# eratos[1] = 0
#
# for i in range(2, int(math.sqrt(len(eratos)))):
#     if eratos[i]:
#         for j in range(i+i, len(eratos), i):
#             eratos[j] = 0
# while True:
#     n = int(sys.stdin.readline())
#
#     if n == 0:
#         break
#     else:
#         print(sum(eratos[n+1:(2*n)+1]))
# import math
#
# def isPrime(num):
#     if num == 1:
#         return False
#     n = int(math.sqrt(num))
#     for i in range(2, n+1):
#         if num % i == 0:
#             return False
#     return True
# lis = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         lis.append(n)
# for n in lis:
#     cnt = 0
#     for i in range(n+1, (2*n)+1):
#         if isPrime(i):
#             print(i)
#             cnt+=1
#     print(cnt)

# import math
# lis = []
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         lis.append(n)
#
# for n in lis:
#     cnt = 0
#     for i in range(n+1, (2*n)+1):
#         if i == 1:
#             break
#         for j in range(2, int(math.sqrt(i))+1):
#             if i % j == 0:
#                 break
#         cnt += 1
#     print(cnt)


