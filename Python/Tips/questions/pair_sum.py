# 정렬 상태에서 오름차순으로 인접 요소 페어를 만들면 가장 큰 페어 합 값이 구해짐
def pair_sum(nums):
    s = 0
    pair = []
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            s += n

    # for n in nums:
    #     pair.append(n)
    #     if len(pair) == 2:
    #         s += min(pair)
    #         pair = []
    return s
