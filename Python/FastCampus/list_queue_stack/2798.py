from itertools import combinations

# BF (3 <= N <= 100) - 300C3
# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
cards = list(map(int, input().split()))


def solution1(n, m, cards):
    result = 0
    for card in combinations(cards, 3):
        card_sum = sum(card)
        if card_sum <= 500:
            result = max(card_sum, result)
    print(result)

    print(result)


def solution2(n, m, cards):
    result = 0
    length = len(cards)

    for i in range(0, length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                sum_value = cards[i] + cards[j] + cards[k]
                if sum_value <= m:
                    result = max(result, sum_value)
    print(result)
