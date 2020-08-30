from collections import Counter
import heapq
nums = list(map(int, list(input())))
k = int(input())
answer = []

cnts = Counter(nums)
for i, v in cnts.items():
    if v >= k:
        answer.append(i)

print(answer)

cnts_heap = []
for f in cnts:
    heapq.heappush(cnts_heap, (-cnts[f], f))

topk = []
# 문제가 다름
# k개 까지 탑 빈도수 출력
for _ in range(k):
    topk.append(heapq.heappop(cnts_heap)[1])

print(topk)

def topK(nums):
    return list(zip(*Counter(nums).most_common(k)))[0]

print(topK(nums))