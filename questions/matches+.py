# 5	5
# 6	7
# 11 99
# 1	0
k = 10


def solution(k):
    numbers = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }

    dp = [0]*51
    for val in numbers.values():
        dp[val] += 1

    print(dp)


solution(k)
