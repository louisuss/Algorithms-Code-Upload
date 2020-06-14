# heap
import heapq

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a + b
    result += sum
    heapq.heappush(heap, sum)

print(result)

# N = int(input())
# card_list = []
# for _ in range(N):
#     card_list.append(int(input()))
# card_list.sort()
# sum = 0
# for i in card_list:
#     sum += i
# for i in range(N-1):
#     sum += card_list[i]
#
# print(sum)