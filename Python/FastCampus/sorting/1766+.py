import heapq

n, m = map(int, input().split())
arr = [[] for i in range(n+1)]  # 인접 리스트
indegree = [0]*(n+1)  # 차수
heap = []  # indegree 0인 최소값 출력
result = []

for _ in range(m):
    # x < y
    x, y = map(int, input().split())
    # 선x 후y
    arr[x].append(y)
    indegree[y] += 1

# 차수 0인 값 힙에 넣기
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

# 힙에서 최소값 뽑음
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    # 현재 데이터에 인접한 값 차수 변경 및 0인 경우 힙 추가
    for y in arr[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)
for i in result:
    print(i, end=' ')
