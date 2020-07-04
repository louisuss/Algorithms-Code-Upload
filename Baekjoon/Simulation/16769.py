C, M = [], []

# 따로 나눠서 가독성이 좋음
for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx = i % 3
    nxt = (i+1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]),
                         0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)


# capacity = []
# state = []


# def mix(p, c, s):
#     if p == 1:
#         if c[1] >= s[0]+s[1]:
#             s[1] = s[0] + s[1]
#             s[0] = 0
#         else:
#             left = (s[0] + s[1]) - c[1]
#             s[1] = c[1]
#             s[0] = left
#     elif p == 2:
#         if c[2] >= s[1]+s[2]:
#             s[2] = s[1] + s[2]
#             s[1] = 0
#         else:
#             left = (s[1] + s[2]) - c[2]
#             s[2] = c[2]
#             s[1] = left
#     else:
#         if c[0] >= s[2]+s[0]:
#             s[0] = s[2] + s[0]
#             s[2] = 0
#         else:
#             left = (s[2] + s[0]) - c[0]
#             s[0] = c[0]
#             s[2] = left

#     return s


# for _ in range(3):
#     a, b = map(int, input().split())
#     capacity.append(a)
#     state.append(b)
# pour = 0

# while pour != 100:
#     pour += 1
#     milk = mix(pour % 3, capacity, state)

# for m in milk:
#     print(m)
