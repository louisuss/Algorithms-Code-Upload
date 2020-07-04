# < > 사이에 있으면 그대로 출력
# 아닌 경우 다음 문자가 ' ' or '<'이면 역순 저장된 단어 역순 출력

S, tmp = input(), ''

ck = False
ans = ''

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + ' '
            tmp = ''
        else:
            ans += ' '
    elif i in '<':
        ck = True
        ans += tmp[::-1] + '<'
        tmp = ''
    elif i in '>':
        ck = False
        ans += '>'
    else:
        if ck:
            ans += i
        else:
            tmp += i
ans += tmp[::-1]
print(ans)

# ck = False
# temp = ''
# for s in S:
#     if s == '<':
#         ck = True
#     if s == '>':
#         ck = False
#         print(temp+s, end='')
#         temp = ''
#         continue

#     if not ck and s == ' ':
#         print(temp[::-1], end=' ')
#         temp = ''
#     if s == '<' and temp:
#         print(temp[::-1], end='')
#         temp = ''
#     if ck:
#         temp += s
#     if not ck and s != ' ':
#         temp += s

# print(temp[::-1], end=' ')
