from collections import Counter

# 중복 문자 제거
# 사전식 순서로 나열


def remove_dupl_char(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + remove_dupl_char(suffix.replace(char, ''))
    return ''

# 스택


def remove_dupl_char2(s):
    # seen - 처리된 문자여부 확인
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        # 뒤에 붙일 문자가 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)
