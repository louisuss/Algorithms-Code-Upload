M = int(input())
N = int(input())
data = list()

for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        data.append(i)

if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(data[0])
# M = int(input())
# N = int(input())
# data = list(range(M, N+1))
# data2 = list()
# sum = 0
# for i in data:
#     cnt = 0
#     for j in range(2, i+1):
#         if i == 1:
#             break
#         if i % j == 0:
#             cnt += 1
#             break
#     if cnt == 1:
#         sum += i
#         data2.append(i)
# if sum == 0:
#     print(-1)
# else:
#     print(sum)
#     print(data2[0])
# def is_prime(nums):
#     lis = list()
#     for i in nums:
#         cnt = 0
#         for k in range(2, i):
#             if i % k == 0:
#                 cnt += 1
#         if cnt == 0:
#             lis.append(i)
#     if len(lis) == 0:
#         return -1
#     else:
#         return lis
#
# M = int(input())
# N = int(input())
# lis = list(range(M,N+1))
# lis = is_prime(lis)
# if lis == -1:
#     print(-1)
# else:
#     print(sum(lis))
#     print(sorted(lis)[0])