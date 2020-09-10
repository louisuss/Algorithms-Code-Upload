from itertools import combinations

l, c = map(int, input().split())
lst = list(input().split())
lst.sort()
vowels = ('a', 'e', 'i', 'o', 'u')

for pwd in combinations(lst, l):
    cnt = 0
    for i in pwd:
        if i in vowels:
            cnt += 1
    if cnt >= 1 and cnt <= l - 2:
        print(''.join(pwd))
