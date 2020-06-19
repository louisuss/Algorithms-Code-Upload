# "(()())()"	"(()())()"
# ")("	"()"
# "()))((()"	"()(())()"
def solution(p):
    def check_right(str):
        cnt = 0
        for i in str:
            if cnt == 0 and i == ')':
                return False
            if i == '(':
                cnt += 1
            else:
                cnt -= 1
        if cnt == 0:
            return True

    def split_uv(str):
        if str == '' or check_right(str):
            return str

        cnt = 0
        u, v = '', ''

        for i in range(len(str)):
            if str[i] == '(':
                cnt += 1
                u += str[i]
            else:
                cnt -= 1
                u += str[i]
            if cnt == 0:
                v += str[i+1:]
                break

        if check_right(u):
            s = split_uv(v)
            return u + s

        else:
            temp = '('
            temp += split_uv(v)
            temp += ')'

            for i in u[1:-1]:
                if i == ')':
                    temp += '('
                else:
                    temp += ')'
            return temp
    return split_uv(p)

# def solution(p):
#     answer = ''

#     def check_right(str):
#         cnt = 0
#         for i in str:
#             if cnt == 0 and i == ')':
#                 return False
#             if i == '(':
#                 cnt += 1
#             else:
#                 cnt -= 1
#         if cnt == 0:
#             return True

#     def split_uv(str):
#         cnt = 0
#         u, v = '', ''
#         if str == '':
#             return ''

#         for i in range(len(str)):
#             if str[i] == '(':
#                 cnt += 1
#                 u += str[i]
#             else:
#                 cnt -= 1
#                 u += str[i]
#             if cnt == 0:
#                 v += str[i+1:]
#                 break

#         res = ''
#         if check_right(u):
#             res += u
#             split_uv(v)
#         else:
#             temp = '('
#             temp += split_uv(v)
#             temp += ')'

#             for i in u[1:-1]:
#                 if i == ')':
#                     temp += '('
#                 else:
#                     temp += ')'
#             res += temp
#         return res
#     answer += split_uv(p)
#     return answer

############

# def solution(p):
#     if p == '':
#         return p
#     r = True
#     c = 0
#     for i in range(len(p)):
#         if p[i] == '(':
#             c -= 1
#         else:
#             c += 1
#         if c > 0:
#             r = False
#         if c == 0:
#             if r:
#                 return p[:i+1]+solution(p[i+1:])
#             else:
#                 return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))
