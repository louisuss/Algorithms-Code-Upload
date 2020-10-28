from itertools import permutations

def check_score(check, num):
    s, b = (0, 0)
    for i in range(3):
        if check[i] == num[i]:
            s += 1
        if check[i] in num:
            b += 1
    return (s,b-s)

def solution(baseball):
    number = [str(x) for x in range(1, 10)]
    allNumber = list(map(''.join, permutations(number, 3)))
    for num, strike, ball in baseball:
        allNumber = [check for check in allNumber if check_score(check,str(num)) == (strike, ball)]

    return len(allNumber)

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))