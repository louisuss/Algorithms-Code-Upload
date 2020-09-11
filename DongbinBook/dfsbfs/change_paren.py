p = input()

# 균형잡힌 괄호 문자열의 인덱스 반환


def balanced_idx(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 괄호 문자열인지 판단
# 시작이 '('이면 올바른 것임. 굳이 함수 필요없음.


def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    idx = balanced_idx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    # if check_proper(u):
    if u[0] == '(':
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # u 문자열 바꾸기 위해서 리스트로 바꿈
        # 문자열로하면 값이 안바뀜
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer


print(solution(p))
# result = ""
# def seperate_uv(value):
#     global result
#     if not value:
#         return value
#     cnt = 0
#     idx = 0
#     for i, val in enumerate(value):
#         if val == '(':
#             cnt += 1
#         else:
#             cnt -= 1
#         if cnt == 0:
#             idx = i
#             break

#     u = value[:idx+1]
#     v = value[idx+1:]
#     if u[0] == '(':
#         return u
#         if v:
#             seperate_uv(v)
#     else:
#         pass
