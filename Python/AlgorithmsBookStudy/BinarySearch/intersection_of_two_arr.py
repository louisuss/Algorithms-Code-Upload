import bisect
# BF
# O(n**2)


def intersection_bf(nums1, nums2):
    result = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return result

# 이진 검색
# 한쪽은 순서대로 탐색, 다른 쪽은 정렬해서 이진 검색으로 값을 찾기
# O(nlogn)


def intersection_bisect(nums1, nums2):
    result = set()
    nums2.sort()
    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        # 해당 값이 있는 인덱스
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
    return result

# 투 포인터 활용
# 정렬: O(nlogn), 비교: O(2n)
# 값이 작은쪽 배열의 포인터가 한 칸씩 앞으로 이동. 어느 한쪽의 포인너가 끝까지 도달하면 종료.


def intersection_two_pointer(nums1, nums2):
    result = set()
    nums1.sort()
    nums2.sort()
    i = j = 0
    # 투 포인터 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        # 같은 경우
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    return result
