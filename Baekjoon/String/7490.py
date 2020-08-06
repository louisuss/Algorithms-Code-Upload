import copy

def recur(arr,n):
    if len(arr) == n:
        operators_list.append(copy.deepcopy(arr))
        return
    arr.append(' ')
    recur(arr, n)
    arr.pop()

    arr.append('+')
    recur(arr, n)
    arr.pop()

    arr.append('-')
    recur(arr,n)
    arr.pop()

test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recur([], n-1)

    ints = [i for i in range(1,n+1)]

    for operators in operators_list:
        string = ""
        for i in range(n-1):
            string+=str(ints[i])+operators[i]
        string+=str(ints[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()