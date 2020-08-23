#     1 2 3
# 1   1 1 1
# 2   1 1 0
# 3   1 0 1

mans, hates = map(int, input().split())
relations = []
for _ in range(mans):
    relations.append(list(map(int, input())))
print(relations)