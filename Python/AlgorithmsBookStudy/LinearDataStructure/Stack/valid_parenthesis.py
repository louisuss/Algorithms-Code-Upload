user_input = input()

def is_valid(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # '(', '{', '[' 저장
        if char not in table:
            stack.append(char)
        # 스택이 빈 경우나 매칭안될때
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

print(is_valid(user_input))