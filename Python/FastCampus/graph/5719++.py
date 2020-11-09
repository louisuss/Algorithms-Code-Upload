from collections import deque
import heapq
import sys
input = sys.stdin.readline

# 최단 경로를 구성하는 간선들을 찾는 방법


def dijkstra():
    heap_data = []
    heapq.heappush(heap_data, (0, start))  # 거리, 위치
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]  # 현재 경로 + 다음결로
            # 제거된 간선들을 고려하지 않기 위해 not dropped[now][i[0]]
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

# 최단 경로에 포함되어 있는 모든 간선을 역으로 추적 할 수 있음
# 0 -> 5 (0 1 2 5) / 5 = distance[2] + cost


def bfs():
    q = deque()
    q.append(end)  # 끝 지점부터 시작

    # 최단경로 역추적
    while q:
        now = q.popleft()
        if now == start:
            continue
        for prev, cost in reverse_adj[now]:
            if distance[now] == distance[prev] + cost:
                dropped[prev][now] = True  # 해당 간선 제외
                q.append(prev)


while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())

    adj = [[] for _ in range(n)]
    reverse_adj = [[] for _ in range(n)]  # 역추적 위한 인접행렬

    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[x].append((y, cost))
        reverse_adj[y].append((x, cost))  # 역으로 경로 추적할 때 사용

    # 제외된 간선 정보 저장
    dropped = [[False] * (n) for _ in range(n)]
    distance = [1e9] * (n)
    dijkstra()  # 최단 경로 탐색
    bfs()  # 최단 경로 삭제
    distance = [1e9] * (n)
    dijkstra()  # 최단 경로 탐색

    if distance[end] != 1e9:
        print(distance[end])
    else:
        print(-1)
