import bisect

# 입력 배열이 정렬되어 있음 -> 투 포인터 활용 가능
# O(n)


def two_sum_twopointer(numbers, target):
    left, right = 0, len(numbers)-1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            # 인덱스가 1부터 시작하는 조건이 있으므로 인덱스 + 1
            return left + 1, right + 1

# 이진 검색
# 현재 값을 기준으로 나머지 값이 맞는지 확인
# O(nlogn)


def two_sum_bisect(numbers, target):
    for k, v in enumerate(numbers):
        # left 는 현재 값 기준 + 1
        left, right = k+1, len(numbers)-1
        expected = target - v
        # 이진 검색으로 나머지 값 판별
        while left <= right:
            mid = left + (right-left)//2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            # mid == expected
            else:
                return k+1, mid+1

# bisect 모듈 + 슬라이싱
# 실행속도가 20배 이상 느려짐


def two_sum_bisect_slicing(numbers, target):
    for k, v in enumerate(numbers):
        expected = target-v
        i = bisect.bisect_left(numbers[k+1:], expected)
        if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
            return k+1, i+k+2

# 성능 개선


def two_sum_bisect_slicing_upgrade(numbers, target):
    for k, v in enumerate(numbers):
        expected = target-v
        nums = numbers[k+1:]
        i = bisect.bisect_left(nums, expected)
        if i < len(nums) and numbers[i+k+1] == expected:
            return k+1, i+k+2

# bisect 모듈 + 슬라이싱 제거
# 투 포인터와 성능 비슷
# 슬라이싱은 편리하고 빠른 모듈이지만 무분별 남용시 속도 저하의 원인
# 슬라이싱은 매번 새롭게 객체를 생성해서 할당. 엄청 큰 배열의 경우 슬라이싱으로 새로운 배열을 생성하는데 많은 시간 소요.


def two_sum_bisect_module(numbers, target):
    for k, v in enumerate(numbers):
        expected = target-v
        i = bisect.bisect_left(numbers, expected, k+1)
        if i < len(numbers) and numbers[i] == expected:
            return k+1, i+1
