from collections import defaultdict
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for next in routes[now]:
            new_dist = distances[now] + 1
            if distances[next] > new_dist:
                distances[next] = new_dist
                heapq.heappush(q, (new_dist, next))

n, m, k, x = map(int, input().split())
routes = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    routes[a].append(b)
MAX = int(1e9)
distances = [MAX]*(n+1)
dijkstra(x)

result = []
for number, distance in enumerate(distances):
    if distance == k:
        result.append(number)

if result:
    for res in result:
        print(res)
else:
    print(-1)