import heapq

n = int(input())
lst = []
result = []

for _ in range(n):
    user_input = int(input())
    if user_input == 0:
        if lst:
            result.append(heapq.heappop(lst))
        else:
            result.append(0)
    else:
        heapq.heappush(lst, user_input)

for res in result:
    print(res)

