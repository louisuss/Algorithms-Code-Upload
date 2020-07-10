def solution(X, Y, D):
    return (Y-X) // D if (Y-X) % D == 0 else (Y-X) // D + 1


# def solution(X, Y, D):
#     cnt = 0
#     while X < Y:
#         X += D
#         cnt += 1
#     return cnt
