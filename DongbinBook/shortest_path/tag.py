import heapq

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

INF = int(1e9)
n, m = map(int, input().split())
house = [[] for _ in range(n+1)]
# 거리 리스트
distance = [0] + [INF] * n

# 헛간 관계
for i in range(m):
    a, b = map(int, input().split())
    house[a].append((b, 1))
    house[b].append((a, 1))


def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in house[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)
m = max(distance)
print(distance.index(m), m, distance.count(m))
