def search(nums, target):
    # 예외 처리
    if not nums:
        return -1

    # 최솟값을 찾아 피벗 설정
    # pivot = nums.index(min(nums))
    left, right = 0, len(nums)-1
    while left < right:
        mid = left + (right-left)//2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left

    # 피봇 기준 이진 검색
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        mid_pivot = (mid+pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid+1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1