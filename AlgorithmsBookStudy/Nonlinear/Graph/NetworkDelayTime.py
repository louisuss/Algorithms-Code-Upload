from collections import deque, defaultdict
import heapq


def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    # 인접리스트
    for u, v, w in times:
        graph[u].append((v, w))

    q = [(0, k)]
    dist = defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

    if len(dist) == n:
        return max(dist.values())
    return -1
