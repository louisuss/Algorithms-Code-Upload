from collections import deque
import re

user_input = input()

# 인자로 list 받음


def is_palindrome(s):
    strs = []
    # 영문자, 숫자 전처리
    for char in s:
        if char.isalnum():
            # 소문자 만들기
            strs.append(char.lower())

    # 양끝을 뽑아서 비교
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def is_palindrome_deque(s):
    strs = deque([])

    for char in s:
        if char.isalnum():
            strs.append(char)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


def is_palindrome_slicing(s):
    s = s.lower()
    # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
    # 문자열 전체를 한 번에 영숫자만 걸러내도록 정규식 처리
    s = re.sub('[^a-z0-9]', '', s)

    # 뒤집은것과 같으면 참
    return s == s[::-1]


print(is_palindrome(user_input))
print(is_palindrome_deque(user_input))
print(is_palindrome_slicing(user_input))
