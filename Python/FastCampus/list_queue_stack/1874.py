# https://www.acmicpc.net/problem/1874
# Stack

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

def solution(n, numbers):
    stack = []
    result = []
    numbers.reverse()

    for n in range(1, n+1):
        stack.append(n)
        result.append("+")

        while stack[-1] == numbers[-1]:
            stack.pop()
            numbers.pop()
            result.append("-")
            if not stack:
                break

    if not numbers:
        for res in result:
            print(res)
    else:
        print("NO")

def solution2(n):
    cnt = 1
    stack = []
    result = []
    for i in range(1, n+1):
        data = int(input())
        while cnt <= data:
            stack.append(cnt)
            cnt += 1
            result.append('+')
        if stack[-1] == data:
            stack.pop()
            result.append('-')
        else:
            print("NO")
            return
    print('\n'.join(result))
    
