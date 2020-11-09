def solution(n):
    answer = [[] for _ in range(n)]
    number = 1
    idx1 = 0
    idx2 = n-1
    direction = 0
    while n > 0:
        if direction == 0:
            for i in range(idx1, idx1+n):
                answer[i].append(number)
                number += 1
            idx1 += 2
        if direction == 1:
            for i in range(n):
                answer[idx2].append(number)
                number += 1
            idx2 -= 1
        if direction == 2:
            print(idx2, idx1-1)
            for i in range(idx2, idx1-2, -1):
                answer[i].append(number)
                number += 1
        n -= 1
        direction = (direction + 1) % 3

    result = []
    for ans in answer:
        if 2 < len(ans) < len(answer):
            ans.append(ans.pop(1))
        result.extend(ans)
    print(answer)
    return result

print(solution(7))