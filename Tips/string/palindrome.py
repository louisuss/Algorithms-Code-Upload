from collections import deque
import re

input_string = input()

# O(n**2)


def is_palindrome(input_string):
    strs = []

    # 영문자, 숫자 여부 판별 후 소문자로 변환
    for char in input_string:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# 최적화 - deque() 활용 (O(n))


def is_palindrome2(input_string):
    strs = deque([])

    for char in input_string:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# 슬라이싱 활용
def is_palindrome3(input_string):
    s = input_string.lower()
    # 정규식으로 불필요한 문자 필터링 (소문자, 숫자 아닌 경우 ''으로 대체)
    s = re.sub('[^a-z0-9]', '', s)
    print(s)

    return s == s[::-1]  # 뒤짚은게 같은지 체크


print(is_palindrome3(input_string))
