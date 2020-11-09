from collections import defaultdict, deque

n, m = map(int, input().split())

arr = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)


def bfs(start):
    q = deque([start])
    visited = [False] * (n+1)
    cnt = 0
    visited[start] = True

    while q:
        now = q.popleft()
        # visited[now] = True
        for next in arr[now]:
            if not visited[next]:
                cnt += 1
                # visited 처리 추가로 안하면 시간초과 발생
                visited[next] = True
                q.append(next)
    return cnt


result = []
for i in range(1, n+1):
    result.append(bfs(i))

max_value = max(result)
for idx, value in enumerate(result, 1):
    if value == max_value:
        print(idx, end=' ')
