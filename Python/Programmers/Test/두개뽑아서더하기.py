from itertools import combinations


def solution(numbers):
    answer = set()
    for case in combinations(numbers, 2):
        answer.add(sum(case))

    return sorted(answer)

