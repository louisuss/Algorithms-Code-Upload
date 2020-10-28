n, m = map(int, input().split())
ricecakes = list(map(int, input().split()))


def cutting(ricecakes, start, end, target):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        s = sum(i-mid for i in ricecakes if i > mid)

        # 딱 맞는 경우 이경우가 최선이므로 리턴
        if s == target:
            return mid
        # 딱맞는 경우가 없을 수도 있으므로 최종 과정 전의 값이 결과임
        elif s > target:
            result = mid
            start = mid + 1
        # 떡이 모자람
        else:
            end = mid - 1

    return result


print(cutting(ricecakes, 0, max(ricecakes), m))
