n = int(input())
arr = list(map(int, input().split()))

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if mid == arr[mid]:
        return mid
    elif mid < arr[mid]:
        return binary_search(arr, start, mid-1)
    else:
        return binary_search(arr, mid+1, end)

idx = binary_search(arr, 0, n-1)

if idx == None:
    print(-1)
else:
    print(idx)