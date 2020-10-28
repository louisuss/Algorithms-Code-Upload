arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot 보다 큰 데이터 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # pivot 보다 작은 데이터 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈린 경우
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            # 작은 데이터 큰데이터 교환
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def quick_sort_pythonic(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽부분

    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)


print(quick_sort_pythonic(arr))
