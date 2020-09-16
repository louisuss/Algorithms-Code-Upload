n = int(input())
coins = list(map(int, input().split()))
coins.sort()

number = 1
for coin in coins:
    if number < coin:
        break
    number += coin

print(number)
