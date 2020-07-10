def make_binary(N):
    s = ''
    while N != 1:
        s = str(N % 2) + s
        N //= 2
    s = '1' + s

    return list(map(int, s))


# def solution(N):
#     cnt = 0
#     answer = 0
#     ck = False
#     N = make_binary(N)

#     for i in range(len(N)):
#         if N[i] == 1:
#             ck = True
#         else:
#             ck = False

#         if not ck:
#             cnt += 1
#         else:
#             answer = max(answer, cnt)
#             cnt = 0
#     return answer
