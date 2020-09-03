import bisect
import sys
sys.setrecursionlimit(10**6)

# O(log n)
# 재귀 활용


def recursive_search(nums, target):
    def binary_search(left, right):
        # 반복 조건
        if left <= right:
            # 반복 행동
            # 자료형을 초과하는 중간위치값 경우 오류 발생
            # mid = (left+right)//2
            mid = left + (right-left)//2

            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return mid
        else:
            return -1
    return binary_search(0, len(nums)-1)

# 반복 활용
# 재귀에 비해 좀 더 직관적


def itinery_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid + 1
        else:
            return mid
    return -1

# 이진 검색 알고리즘 활용


def bisect_search(nums, target):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1

# index() 메소드 활용
# O(n)


def index_search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1
