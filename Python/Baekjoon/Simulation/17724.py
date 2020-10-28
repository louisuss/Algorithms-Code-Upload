# 문제수 / 역량 / 최대 개수
N, L, K = map(int, input().split())

# 쉬운문제 / 어려운문제
easy, hard = 0, 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K) * 140

if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)

# q = []

# for _ in range(N):
#     q.append(list(map(int, input().split())))
# q.sort(key=lambda x: x[1], reverse=True)

# score = 0

# for _ in range(K):
#     if q[-1][1] > L:
#         q.sort(key=lambda x: x[0], reverse=True)
#         a = q.pop()
#         if a[0] <= L:
#             score += 100
#         else:
#             break
#     else:
#         q.pop()
#         score += 140
# print(score)
