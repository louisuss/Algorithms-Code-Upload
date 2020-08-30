from collections import Counter
import heapq


def top_k_freq(nums, k):
    freqs = Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = []
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


def find_kth_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


def find_kth_largest2(nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

# nlargest


def find_kth_largest3(nums, k):
    return heapq.nlargest(k, nums)[-1]

# 정렬이용


def find_kth_largest4(nums, k):
    return sorted(nums, reverse=True)[k-1]
