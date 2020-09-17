from itertools import permutations
from copy import deepcopy

# 6
# 1 2 3 4 5 6
# 2 1 1 1

# 3
# 3 4 5
# 1 0 1 0

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

# Solution 1 - bf
op_kinds = ['+', '-', '*', '//']
op_cases = []
for op in zip(op_kinds, operators):
    # [['+', '+'], ['-'], ['*'], ['//']]
    # op_cases.append([op[0]]*op[1])
    op_cases.extend([op[0]]*op[1])

max_result = -int(1e9)
min_result = int(1e9)
# 모든 경우의 수
for cases in permutations(op_cases, n-1):
    copy_numbers = deepcopy(numbers)
    # 누적값
    res = copy_numbers.pop(0)
    for case in cases:
        # 연산할 값
        next_number = copy_numbers.pop(0)
        if case == '+':
            res = res + next_number
        elif case == '-':
            res = res - next_number
        elif case == '*':
            res = res * next_number
        else:
            # 현재값이 음수인 경우 조건에 맞게 변경
            # if res < 0:
            #     res = abs(res) // next_number
            #     res = -res
            res = res // next_number  # 위 조건과 같음
            # else:
            #     res = res // next_number
    max_result = max(max_result, res)
    min_result = min(min_result, res)

print(max_result)
print(min_result)


max_result = -int(1e9)
min_result = int(1e9)
add, sub, mul, div = operators

# Solution 2 - dfs
# 이 경우 조건문에서 항상 + 부터 시작하는 것 같아 오답인듯함.


def dfs(i, now):
    global min_result, max_result, add, sub, mul, div

    # 모든 연산자 다 사용한 경우
    if i == n:
        min_result = min(min_result, now)
        max_result = max(max_result, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + numbers[i])
            # 다른 경우에서도 사용해야되기 떄문에 다시 복구
            add += 1
        elif sub > 0:
            sub -= 1
            dfs(i+1, now - numbers[i])
            sub += 1
        elif mul > 0:
            mul -= 1
            dfs(i+1, now * numbers[i])
            mul += 1
        else:
            div -= 1
            dfs(i+1, now // numbers[i])
            div += 1


dfs(1, numbers[0])

print(max_result)
print(min_result)
