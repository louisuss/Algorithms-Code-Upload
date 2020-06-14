# Bottom-up 방식
n = int(input())
d = [0] * (n+1)
d[1] = 0
for i in range(2, n+1):
    # +1
    d[i] = d[i-1]+1
    # /2 한 경우, +1 은 / 연산 횟수 추가한 것
    if i%2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2]+1
    # /3 한 경우, +1 은 / 연산 횟수 추가한 것
    if i%3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3]+1
print(d[n])

# x = int(input())
#
# min_cnt = [0] * (x+1)
# idx = 0
# while True:
#     if idx > x:
#         break
#     if idx <= 1:
#         min_cnt[idx] = 0
#     else:
#         temp_min = x+1
#         if idx % 3 == 0:
#             temp_idx = int(idx/3)
#             temp_min = min(temp_min, min_cnt[temp_idx])
#
#         if idx % 2 == 0:
#             temp_idx = int(idx/2)
#             temp_min = min(temp_min, min_cnt[temp_idx])
#         temp_min = min(temp_min, min_cnt[idx-1])
#         min_cnt[idx] = int(temp_min+1)
#     idx = idx + 1
# print(min_cnt[x])