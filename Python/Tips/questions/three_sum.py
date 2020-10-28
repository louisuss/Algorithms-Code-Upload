# 투포인터
def three_sum(nums):
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        # 중복제거?
        if nums[i] == nums[i-1]:
            continue

        # 간격 좁히며 합 계산
        left, right = i+1, len(nums)-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                # s == 0 인 경우
                results.append((nums[i], nums[left], nums[right]))

                # 다음값과 같은 경우 이동
                while left < right and nums[left] == nums[left+1]:
                    left += 1

                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                # 이동
                left += 1
                right -= 1
    return results
