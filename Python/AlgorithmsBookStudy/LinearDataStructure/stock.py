import sys
# O(n**2)


def max_profit(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(price[j] - price, max_price)
    return max_price

# O(n)


def max_profit2(prices):
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)

    return profit
