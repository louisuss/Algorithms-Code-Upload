def see_trophy(arr):
    max = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] > max:
            cnt += 1
            max = arr[i]
    return cnt


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
# numbers = [int(input()) for _ in range(n)]

print(see_trophy(numbers))
numbers.reverse()
print(see_trophy(numbers))
# print(see_trophy(sorted(numbers, reverse=True))) - Error
