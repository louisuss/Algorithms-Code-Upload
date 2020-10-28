# 투포인터
def trap(heights):
    if not heights:
        return 0

    volume = 0
    left, right = 0, len(heights)-1
    left_max, right_max = heights[left], heights[right]

    while left <= right:
        left_max, right_max = max(heights[left], left_max), max(
            heights[right], right_max)

        # 더 높은쪽으로 이동
        if left_max <= right_max:
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1
    return volume

# 스택


def trap2(heights):
    stack = []  # 인덱스 추가
    volume = 0

    for i in range(len(heights)):
        # 변곡점 만나는 경우
        while stack and heights[i] > heights[stack[-1]]:
            # 스택에서 꺼내기
            top = stack.pop()

            # 스택이 없으면 종료
            if not len(stack):
                break

            # 이전과의 차이만큼 물높이 처리
            distance = i - stack[-1] - 1
            waters = min(heights[i], heights[stack[-1]]) - heights[top]

            volume += distance * waters

        stack.append(i)
    return volume
