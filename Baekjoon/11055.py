from copy import deepcopy

n = int(input())
a = list(map(int, input().split()))
# dp[i] : i 까지 왔을 때, 합의 최대
dp = deepcopy(a)
rev = [i for i in range(n)]

idx = 0

# for i in range(1, n):
#     for j in range(i):
#         if a[i] > a[j]:
#             dp[i] = max(a[i] + dp[j], dp[i])
#
# # 문제1
# print(max(dp))

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < a[i] + dp[j]:
            dp[i] = a[i] + dp[j]
            rev[i] = j
    if dp[idx] < dp[i]:
        idx = i

print(dp)
print(max(dp))

print(rev)

# 문제2 : 최대일때의 리스트 출력
print(dp[idx])
while rev[idx] != idx:
    print(a[idx], sep=' ')
    idx = rev[idx]

print(a[idx])
