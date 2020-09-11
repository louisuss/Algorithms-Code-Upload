# 5
# 2 1 2 6 2 4 3 3

n = int(input())
stages = list(map(int, input().split()))
stages.sort()
length = len(stages)
answer = []
for i in range(1, n+1):
    cnt = stages.count(i)
    if length == 0:
        fail = 0
    else:
        fail = cnt / length
    answer.append((i, fail))
    length -= cnt
answer = sorted(answer, key=lambda t: t[1], reverse=True)
answer = [i[0] for i in answer]

# result = []
# for stage in range(1, n+1):
#     arrive_stage = 0
#     not_clear = 0
#     for i in stages:
#         if i >= stage:
#             arrive_stage += 1
#         if i == stage:
#             not_clear += 1
#     result.append((stage, not_clear/arrive_stage))

# result = sorted(result, key=lambda x: (-x[1], x[0]))
# new_result = []
# for res in result:
#     new_result.append(res[0])
# print(new_result)
