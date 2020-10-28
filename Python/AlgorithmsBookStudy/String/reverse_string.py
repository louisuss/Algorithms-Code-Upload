user_input = list(input())

# 1. 투 포인터 이용한 스왑


def reverse_string(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1


# 2. 파이썬 방식
# reverse -> 리스트에서만 제공
user_input.reverse()

# 3. 슬라이싱 활용 -> 공간 복잡도 O(1) 제한이 주어진 경우 변수 할당을 처리하는 데 제약 존재
# user_input = user_input[::-1] # 이 경우 제한 조건 만족 못함
user_input[:] = user_input[::-1]  # 제한 조건 패스
