# import copy

# result = []
# string = []
# visited = []

# def combination(array, length, index):
#     # 길이가 length인 모든 조합 찾기
#     if len(string) == length:
#         result.append(copy.deepcopy(string))
#         return
    
#     # 각 원소를 한 번씩만 뽑도록 구성
#     for i in range(index, len(array)):
#         if i in visited:
#             continue
#         string.append(array[i])
#         visited.append(i)
#         combination(array, length, i+1)
#         string.pop()
#         visited.pop()


# vowels = ['a', 'e', 'i', 'o', 'u']
# l, c = map(int, input().split())
# array = input().split(' ')
# array.sort()

# combination(array, l, 0)

# # 길이가 1인 모든 암호 조합 확인
# for pwd in result:
#     cnt = 0
#     # 모음 개수 세기
#     for i in pwd:
#         if i in vowels:
#             cnt += 1
#     if cnt >= 1 and cnt <= l - 2:
#         print(''.join(pwd))

from itertools import combinations
# 최소 한개의 모음 두개 자음
# 알파벳이 증가
# [a, e, i, o, u]
L, C = map(int, input().split())
A = sorted(list(input().split(' ')))
vowels = ['a', 'e', 'i', 'o', 'u']

for pwd in combinations(A, L):
    cnt = 0
    for i in pwd:
        if i in vowels:
            cnt += 1
    if 1 <= cnt and cnt <= L-2:
        print(''.join(pwd))

