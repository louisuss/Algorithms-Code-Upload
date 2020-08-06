# n = int(input())
# books = {}
#
# for _ in range(n):
#     book = input()
#     if book not in books:
#         books[book] = 1
#     else:
#         books[book] += 1
#
# target = max(books.values())
# arr = []
#
# for book, number in books.items():
#     if number == target:
#         arr.append(book)
# print(sorted(arr)[0])

from collections import Counter

sold = int(input())
book_list = []
for _ in range(sold):
    book_list.append(input())

count = Counter(book_list)
target = max(count.values())
arr = []
for book, number in count.items():
    if number == target:
        arr.append(book)
print(sorted(arr)[0])


# n = int(input())
# books = []
# for _ in range(n):
#     books.append(input())

# top_books = []
# # 숫자 세기
# books = Counter(books)
# m = max(books.values())
# for book in books:
#     # book = key
#     # 가장 많은 것 리스트에 담기
#     if books[book] == m:
#         top_books.append(book)

# print(sorted(top_books)[0])
