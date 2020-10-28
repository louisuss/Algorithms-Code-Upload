from collections import Counter, defaultdict

n = int(input())
lst = [input() for _ in range(n)]
result = defaultdict(int)

for l in lst:
    result[l] += 1
result = result.items()
print(sorted(result, key=lambda x: (-x[1], x[0]))[0][0])

books = Counter(sorted(lst)).items()
books = sorted(books, key=lambda x: (-x[1], x[0]))
print(books[0][0])

# print(books.most_common(1)[0][0])
