import heapq

n = int(input())
q = []

for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) >= 2:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    sum_value = a + b
    result += sum_value
    heapq.heappush(q, sum_value)

# n == 1 인 경우는 비교할 수 없으므로 0임
print(result)
