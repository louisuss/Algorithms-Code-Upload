# 1 2 3 3 4
n = int(input())
afraid = list(map(int, input().split()))
afraid.sort()
result = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in afraid:
    cnt += 1
    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
    if cnt >= i:
        result += 1
        cnt = 0
print(result)

# # 필요한 인원 체크
# for i in afraid:
#     cnt = 0
#     while cnt < i:
#         # i만큼 afraid에서 제거
#         temp = 0
#         if afraid:
#             temp = afraid.pop()
#         else:
#             break
#         if temp > i:
#             i = temp
#         cnt += 1
#     print(afraid)

#     result += 1
# print(cnt)

