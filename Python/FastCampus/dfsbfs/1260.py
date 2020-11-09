from collections import deque
n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]


# visited 처리 위치 헷갈림.

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for next in adj[start]:
        if not visited[next]:
            dfs(next)

def bfs(start):
    q = deque([start])
    visited[start] = True
    print(start, end=' ')
    while q:
        now = q.popleft()
        for next in adj[now]:
            if not visited[next]:
                # 이 부분에서 방문처리 안하면 4가 두번 더 출력됨
                visited[next] = True
                print(next, end=' ')
                q.append(next)


# def bfs(start):
#     q = deque([start])
#     while q:
#         now = q.popleft()
#         if not visited[now]:
#             visited[now] = True
#             print(now, end=' ')
#             for next in adj[now]:
#                 if not visited[next]:
#                     q.append(next)

# 행 마다 정렬 수행 - 저장됨
for i in adj:
    i.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

