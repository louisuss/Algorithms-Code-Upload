from collections import deque

# BF


def max_sliding_window(nums, k):
    if not nums:
        return nums
    r = []
    for i in range(len(nums)-k+1):
        r.append(max(nums[i:i+k]))
    return r

# 정렬되지 않은 슬라이딩 윈도우에서 최댓값 추출하려면 무조건 한번 이상은 봐야함


def max_sliding_window2(nums, k):
    result = []
    window = deque([])
    INF = float('-inf')
    max_val = INF
    for i, num in enumerate(nums):
        window.append(num)
        # 윈도우 크기
        if i < k-1:
            continue

        # 새로 추가된 값이 기존의 최대값보다 큰 경우 교체
        if max_val == INF:
            max_val = max(window)
        elif num > max_val:
            max_val = num

        result.append(max_val)
        # 다음에 빼는 숫자가 가장 큰값인 경우
        if max_val == window.popleft():
            max_val = INF
    print(result)


nums = list(map(int, input().split()))
k = int(input())
max_sliding_window(nums, k)
