from collections import defaultdict
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for result in results:
        # 키 = 패자 / 값 = 승자
        lose[result[1]].add(result[0])
        # 키 = 승자 / 값 = 패자
        win[result[0]].add(result[1])

    for i in range(1, n+1):
        for winner in lose[i]:
            # win[i]: 승자 i가 이긴 패자 추가
            win[winner].update(win[i])
        for loser in win[i]:
            # lose[i]: 패자 i가 진 승자 추가
            lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == (n-1):
            print(1)
            answer += 1

    return answer


solution(n, results)
