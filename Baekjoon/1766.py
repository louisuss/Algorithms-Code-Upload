# heap
import heapq

n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
indegree = [0] * (n+1)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    # node 연결
    arr[x].append(y)
    # 진입차수
    indegree[y] += 1

for i in range(1, n+1):
    # 진입 차수 0인 정점을 큐에 삽입
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

# 큐에서 원소를 꺼내 해당 원소와 간선을 제거
# 제거 이후 진입 차수가 0이 된 정점을 큐에 삽입
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in arr[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)
for i in result:
    print(i, end=' ')