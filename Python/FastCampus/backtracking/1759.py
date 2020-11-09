from itertools import combinations

L, C = map(int, input().split())
possible_char = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
possible_char.sort()

for case in combinations(possible_char, L):
    cnt_vowel = 0
    cnt_consonant = 0
    for char in case:
        if char in vowels:
            cnt_vowel += 1
        else:
            cnt_consonant += 1

    if cnt_vowel >= 1 and cnt_consonant >= 2:
        print(''.join(case))

print()

result = []
string = []
visited = []

# combination 구현 !!


def combination(possible_char, length, index):
    if len(string) == length:
        # deepcopy를 추가해야함.
        result.append(string[:])
        return

    for i in range(index, len(possible_char)):
        if i in visited:
            continue
        string.append(possible_char[i])
        visited.append(i)  # 중복 제거
        combination(possible_char, length, i + 1)
        string.pop()  # 사용 후 제거
        visited.pop()  # 사용 후 제거


combination(possible_char, L, 0)

for password in result:
    cnt_vowel = 0
    for i in password:
        if i in vowels:
            cnt_vowel += 1
    if cnt_vowel >= 1 and cnt_vowel <= L-2:
        print(''.join(password))
