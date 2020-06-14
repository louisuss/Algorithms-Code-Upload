n = int(input())
dp = [0]
nums = [0]
for _ in range(n):
    nums.append(int(input()))

dp.append(nums[1])
if n > 1:
    dp.append(nums[1]+nums[2])
for i in range(3, n+1):
    # 1. 안먹음 2. 전전전 dp + 전꺼먹음 + 지금먹음 3. 전전꺼 dp + 지금먹음
    dp.append(max(dp[i-1], dp[i-3] + nums[i-1]+ nums[i], dp[i-2] + nums[i]))
print(dp[n])
