# 연속된 수
def solution(n):
    answer = 0
    for start in range(1, n):
        sum = 0
        if start > n // 2:
            answer += 1
            break
        for i in range(start, n):
            sum += i
            if sum == n:
                answer += 1
                break
            if sum > n:
                break
    return answer
