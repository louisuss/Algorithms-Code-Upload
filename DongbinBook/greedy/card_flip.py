s = input()

start = s[0]
lst = [s[0]]

# Solution1
# 그룹 지어서 더 적은 그룹횟수만큼 뒤집으면 됨
for i in range(1, len(s)):
    if start != s[i]:
        start = s[i]
        lst.append(start)

print(min(lst.count('1'), lst.count('0')))

# Solution2
# 0으로바꾸는경우, 1로바꾸는경우
cnt0, cnt1 = 0, 0

# 첫번째 원소 처리
if s[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        # 다음수가 1로 바뀌는 경우
        if s[i+1] == '1':
            cnt0 += 1
        # 다음수가 0으로 바뀌는 경우
        else:
            cnt1 += 1
print(min(cnt0, cnt1))
