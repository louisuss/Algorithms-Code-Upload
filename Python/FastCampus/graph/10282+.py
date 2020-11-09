from collections import defaultdict
import heapq


def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))  # 초기값 대입. (시간, 위치)
    times[start] = 0

    while heap_data:
        time, now = heapq.heappop(heap_data)
        if times[now] < time:
            continue
        for next in adj[now]:
            # 다음 시간 갱신 여부 계산 (현재 시간 + 다음 시간, 다음 위치 시간)
            total = time + next[1]
            if times[next[0]] > total:
                times[next[0]] = total
                heapq.heappush(heap_data, (total, next[0]))


t = int(input())
MAX = 1e9
for _ in range(t):
    n, d, start = map(int, input().split())
    adj = [[] for i in range(n+1)]
    times = [MAX] * (n+1)  # 시간 갱신 테이블

    for _ in range(d):
        a, b, time = map(int, input().split())
        adj[b].append((a, time))

    dijkstra(start)

    cnt = 0
    max_time = 0
    for i in times:
        # 시간이 갱신된적이 있는 경우
        if i != MAX:
            # 감염 추가
            cnt += 1
            # 최대 시간 갱신
            if i > max_time:
                max_time = i

    print(cnt, max_time)
