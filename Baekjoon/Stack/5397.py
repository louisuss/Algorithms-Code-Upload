# O(n) 풀어야 함
# 1. 스택 두개만듬. 커서를 중간에 있다 가정
# 2. - : 왼쪽스택에서 원소삭제
# 3. < : 왼쪽 -> 오른쪽 원소 이동
# 4. > : 오른쪽 -> 왼쪽 원소 이동
t = int(input())

for _ in range(t):
    key_log = input()
    left_stk = []
    right_stk = []

    for log in key_log:
        if log == '-':
            if left_stk:
                left_stk.pop()
        elif log == '<':
            if left_stk:
                right_stk.append(left_stk.pop())
        elif log == '>':
            if right_stk:
                left_stk.append(right_stk.pop())
        else:
            left_stk.append(log)
    # right_stk 뒤집어야함
    right_stk.reverse()
    pwd = left_stk+right_stk
    print(''.join(pwd))
