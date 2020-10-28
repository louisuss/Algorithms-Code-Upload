# n = int(input())
# s = input()
# ans = 0
# bonus = 0
# for i in range(len(s)):
#     if s[i] == 'O':
#         bonus += 1
#         ans += i + bonus
#     elif s[i] == 'X':
#         bonus = 0
# print(ans)

n, s = input(), input()

score, bonus = 0, 0

for idx, ox in enumerate(s):
    if ox == 'O':
        score, bonus = score+idx+1+bonus, bonus+1
    else:
        bonus = 0

print(score)

