from math import sqrt

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    xy_d = sqrt((x2-x1)**2 + (y2-y1)**2)
    r_d1 = abs(r2 - r1)
    r_d2 = r1 + r2

    if xy_d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if xy_d == r_d1 or xy_d == r_d2:
            print(1)
        elif xy_d < r_d1 or xy_d > r_d2:
            print(2)
        else:
            print(0)






# from math import sqrt
#
# test = int(input())
# for _ in range(test):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     # 원의 중심 사이 거리
#     d = sqrt(((x2-x1)**2 + (y2-y1)**2))
#     rs = r1 + r2
#     rm = abs(r1-r2)
#
#     if d == 0:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#
#     else:
#         if d == rs or d == rm:
#             print(1)
#         elif d < rs and d > rm:
#             print(2)
#         else:
#             print(0)
