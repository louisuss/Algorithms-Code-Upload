n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
max_card = 0

for i in range(n):
    max_card = max(max_card, min(cards[i]))
print(max_card)