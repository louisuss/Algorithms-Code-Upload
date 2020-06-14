from itertools import permutations

def solution(n, weak, dist):
    weak_length = len(weak)

    # 길이를 두 배 늘려놓으면 방향 고민 필요없음
    for i in range(weak_length):
        weak.append(weak[i]+n)

    answer = len(dist) + 1
    for i in range(weak_length):
        start_point = [weak[j] for j in range(i, i+weak_length)]

        candidates = permutations(dist, len(dist))

        for order in candidates:



