import bisect

i = [1, 1, 2, 3, 3]

print(bisect.bisect_left(i, 2))
print(bisect.bisect_right(i, 2))