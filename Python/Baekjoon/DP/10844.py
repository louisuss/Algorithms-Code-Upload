# n = int(input())
# dp = [[] for _ in range(101)]
# dp[1] = [[i] for i in range(1,10)]
# for i in range(2,n+1):
#     for start_idx in dp[i-1]:
#         if start_idx[-1] == 9:
#             dp[i].append(start_idx.append(start_idx[-1] - 1))
#         else:
#             dp[i].append(start_idx.append(start_idx[-1] + 1))
#             dp[i].append(start_idx.append(start_idx[-1] - 1))
#
# print(len(dp[n]))

n = int(input())
max = 100
mod = 1000000000
dp = [[0]*10 for _ in range(max+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, max+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%mod)


