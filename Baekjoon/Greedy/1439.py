# 0 1 : 0, 0(바뀌는 구간)
# 01 10 : 1, 1
# 101, 010 : 1, 2
# 1010 : 2, 3
# 10101 : 2, 4
# 101010 : 3, 5
# (바뀌는 구간 개수 + 1) // 2
S, total = input(), 0

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        total += 1
print((total+1)//2)


# from collections import Counter

# S = input()


# def solution(S):
#     if S == "0"*len(S) or S == "1"*len(S):
#         return 0
#     else:
#         c = Counter(S)
#         cn = c.most_common(2)[1][0]
#         check = False
#         cnt = 0
#         for i in S:
#             if i == cn and check == False:
#                 cnt += 1
#                 check = True
#             if i != cn:
#                 check = False
#         return cnt


# print(solution(S))
