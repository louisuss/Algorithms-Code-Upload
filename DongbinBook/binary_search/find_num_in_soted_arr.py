import bisect

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Solution 1
start_idx = bisect.bisect_left(arr, x)
end_idx = bisect.bisect_right(arr, x)

# start_idx 가 범위 넘을 수 있음.
if start_idx >= n or arr[start_idx] != x:
    print(-1)
else:
    print((end_idx-start_idx))

# Solution 2


def cnt_by_range(arr, left_val, right_val):
    right_idx = bisect.bisect_right(arr, right_val)
    left_idx = bisect.bisect_left(arr, left_val)
    # 없는 경우 0
    return right_idx-left_idx


cnt = cnt_by_range(arr, x, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)

# Solution 3


def count_x(arr, target):
    n = len(arr)

    # x가 처음 등장한 인덱스
    first = find_first_idx(arr, x, 0, n-1)

    # x가 존재하지 않는 경우
    if first == None:
        return 0

    last = find_last_idx(arr, x, 0, n-1)

    return last-first+1


def find_first_idx(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        return find_first_idx(arr, target, start, mid - 1)
    else:
        return find_first_idx(arr, target, mid+1, end)


def find_last_idx(arr, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    if (mid == n-1 or target < arr[mid+1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return find_last_idx(arr, target, start, mid - 1)
    else:
        return find_last_idx(arr, target, mid+1, end)


cnt = count_x(arr, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)
