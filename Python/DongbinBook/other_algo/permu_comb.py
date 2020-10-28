from itertools import permutations, combinations
data = [1, 2]
for x in permutations(data, 2):
    print(list(x))

data = [1, 2, 3]
for x in combinations(data, 2):
    print(list(x), end=' ')
