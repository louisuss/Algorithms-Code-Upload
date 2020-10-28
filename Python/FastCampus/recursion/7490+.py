from copy import deepcopy
from itertools import product

t = int(input())


# Solution1
# 연산자의 가능한 모든 조합 연산
def makeZero(arr, n):
    if len(arr) == n:
        # deepcopy 안하면 arr에 계속 누적되서 인덱스 초과 발생 
        operators_list.append(deepcopy(arr))
        return
    arr.append(' ')
    makeZero(arr, n)
    arr.pop()
    arr.append('+')
    makeZero(arr, n)
    arr.pop()
    arr.append('-')
    makeZero(arr, n)
    arr.pop()


for _ in range(t):
    n = int(input())
    operators_list = []

    makeZero([], n-1)
    integers = [i for i in range(1, n+1)]
    for operator in operators_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operator[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()

# Solution2
for _ in range(t):
    n = int(input())
    op_list = [' ', '+', '-']
    operators = []
    for op in product(op_list, repeat=n-1):
        operators.append(op)

    numbers = [i for i in range(1, n+1)]
    for op in operators:
        string = ""
        # 1 +
        for i in range(n-1):
            string += str(numbers[i]) + op[i]
        # 1 + 3
        string += str(numbers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()
