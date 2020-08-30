from collections import defaultdict
import heapq


def findCheapestFlights(n, flights, src, dst, k):
    graph = defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 가격, 정점, 남은 가능 경유지 수
    q = [(0, src, k)]

    while q:
        price, node, k = heapq.heappop(q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(q, (alt, v, k-1))
    return -1
