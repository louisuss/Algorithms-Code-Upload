def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    left_idx, right_idx, idx = 0,0,0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            arr[idx] = left[left_idx]
            left_idx+=1
        else:
            arr[idx] = right[right_idx]
            right_idx+=1
        idx+=1

    if left_idx == len(left):
        while right_idx < len(right):
            arr[idx] = right[right_idx]
            right_idx+=1
            idx+=1
    elif right_idx == len(right):
        while left_idx < len(left):
            arr[idx] = left[left_idx]
            left_idx+=1
            idx+=1
    return arr

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr = merge_sort(arr)

for data in arr:
    print(data)