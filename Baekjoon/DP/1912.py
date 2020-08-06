n = int(input())
nums = list(map(int, input().split()))

sum = 0
max = nums[0]
for num in nums:
    sum += num

    if sum > 0:
        if max < sum:
            max = sum
    else:
        if max < num:
            max = num
        else:
            sum = 0

print(max)

