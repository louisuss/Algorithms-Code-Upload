from collections import deque

# BF


def max_sliding_window(nums, k):
    if not nums:
        return nums

    r = []
    for i in range(len(nums)-k+1):
        r.append(max(nums[i:i+k]))
    return r

# deque


def max_sliding_window_q(nums, k):
    results = []
    window = deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        # 기존 최대값을 기억해뒀다 활용
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
    return results


print(max_sliding_window_q([1, 3, -1, -3, 5, 3, 6, 7], 3))
