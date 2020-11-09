# 500, 100 50, 10, 5, 1
# 큰 순서대로 나누기
# 코인 누적
# 다 나눠졌으면 break
paid = int(input())
need_get = 1000 - paid

total_coin = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    if need_get == 0:
        break
    total_coin += need_get // coin
    need_get %= coin

print(total_coin)
