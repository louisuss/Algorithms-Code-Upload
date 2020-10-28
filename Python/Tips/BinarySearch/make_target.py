import bisect

# 투포인터 - 정렬 조건 필요


def two_sum(numbers, target):
    # 양 끝에서 출발
    left, right = 0, len(numbers) - 1
    while left <= right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left + 1, right + 1  # 인덱스가 1 부터 시작하기 때문

# 현재값 기준 -> 나머지 값이 존재하는지 확인


def two_sum2(numbers, target):
    for i, v in enumerate(numbers):
        # 현재 인덱스 다음 = i+1
        left, right = i + 1, len(numbers)-1
        expected = target - v

        # 이진 검색 -> 나머지값찾기
        while left <= right:
            mid = left + (right-left)//2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return i+1, mid+1

# bisect 활용
# two_sum3_1, two_sum3_2 에서 슬라이싱이 사용되서 속도가 느림.


def two_sum3_1(numbers, target):
    for i, v in enumerate(numbers):
        expected = target-v
        # idx = i+1 위치를 0으로 해서 구한 인덱스이므로 나중에 i+1 해줘야됨
        idx = bisect.bisect_left(numbers[i+1:], expected)
        if idx < len(numbers[i+1:]) and numbers[idx+(i+1)] == expected:
            return i+1, idx+i+2


def two_sum3_2(numbers, target):
    for i, v in enumerate(numbers):
        expected = target-v
        nums = numbers[i+1:]
        # idx = i+1 위치를 0으로 해서 구한 인덱스이므로 나중에 i+1 해줘야됨
        idx = bisect.bisect_left(nums, expected)
        if idx < len(nums) and numbers[idx+(i+1)] == expected:
            return i+1, idx+i+2


def two_sum3_3(numbers, target):
    for i, v in enumerate(numbers):
        expected = target-v
        # 슬라이싱 사용하지 않고 i+1로 왼쪽 범위를 제한
        idx = bisect.bisect_left(numbers, expected, i+1)
        if idx < len(numbers) and numbers[idx] == expected:
            return i+1, idx+1
