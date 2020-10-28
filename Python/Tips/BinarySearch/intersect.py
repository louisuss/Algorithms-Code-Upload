import bisect

# BF (n**2)


def intersection(nums1, nums2):
    result = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return list(result)

# 한쪽은 순차 탐색, 다른 한쪽은 이진 검색 nlog(n)


def intersection2(nums1, nums2):
    result = set()
    nums2.sort()

    for n1 in nums1:
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) < i2 and n1 == nums2[i2]:
            result.add(n1)
    return result

# 투포인터 nlog(n)


def intersection3(nums1, nums2):
    result = set()
    nums1.sort()
    nums2.sort()
    i = j = 0

    # 투 포인터 우측으로 이동하며 일치여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    return result
