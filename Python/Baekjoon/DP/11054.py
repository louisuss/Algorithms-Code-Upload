n = int(input())
nums = list(map(int, input().split()))
inc = [1 for _ in range(n)]
dec = [1 for _ in range(n)]
res = [0 for _ in range(n)]

# increase
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and inc[i] < inc[j] + 1:
            inc[i] = inc[j] + 1

# decrease
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if nums[i] > nums[j] and dec[i] < dec[j]+1:
            dec[i] = dec[j] + 1
    res[i] = dec[i] + inc[i] - 1
print(max(res))



