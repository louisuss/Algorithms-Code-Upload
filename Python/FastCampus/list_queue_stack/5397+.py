# https: //www.acmicpc.net/problem/5397
# 키로그 문제
t = int(input())
str = []
for _ in range(t):
    str.append(input())


def backspace(idx):
    if idx > 0:
        return idx-1
    else:
        return 0


def move(idx, key_length):
    if key_length > idx:
        return idx+1
    else:
        return idx


def solution(t, str):
    for s in str:
        idx = 0
        data = ""
        for char in s:
            if char == '<':
                idx = backspace(idx)
            elif char == '>':
                idx = move(idx, len(data))

            # - 부분 idx 부분 해결이 오래걸림
            elif char == '-':
                if data:
                    idx = backspace(idx)
                    data = data[:idx] + data[idx+1:]
            else:
                data = data[:idx] + char + data[idx:]
                idx = move(idx, len(data))
        print(data)


def solution2(t, str):
    left_stack = []
    right_stack = []

    for s in str:
        for char in s:
            if char == '-':
                if left_stack:
                    left_stack.pop()
            elif char == '<':
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif char == '>':
                if right_stack:
                    left_stack.append(right_stack.pop())
            else:
                left_stack.append(char)
        left_stack.extend(reversed(right_stack))
        print(''.join(left_stack))


solution(t, str)
