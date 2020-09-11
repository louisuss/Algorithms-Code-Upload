n = int(input())
homes = list(map(int, input().split()))
homes.sort()
# 중간에 위치해 있을 때 가장 최선
print(homes[(n-1)//2])

# min_home = min(homes)
# max_home = max(homes)
# INF = int(1e9)
# dp = [INF] * (max_home+1)
# for i in range(min_home, max_home+1):
#     sum = 0
#     for j in homes:
#         sum += abs(i-j)
#     dp[i] = sum

# print(dp.index(min(dp)))
