from collections import defaultdict, Counter


def nums_jewels(J, S):
    freqs = {}
    cnt = 0

    # 돌 빈도수
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # 보선 빈도수
    for char in J:
        if char in freqs:
            cnt += freqs[char]

    return cnt


def nums_jewels2(J, S):
    freqs = defaultdict(int)
    cnt = 0

    for char in S:
        freqs += 1

    for char in J:
        cnt += freqs[char]

    return cnt


def nums_jewels3(J, S):
    freqs = Counter(S)
    cnt = 0

    for char in J:
        cnt += freqs[char]

    return cnt


def nums_jewels4(J, S):
    return sum(s in J for s in S)
