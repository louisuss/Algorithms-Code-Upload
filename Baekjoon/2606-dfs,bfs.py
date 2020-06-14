# from collections import deque
#
# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if not visited[v]:
#             visited[v] = True
#             for e in adj[v]:
#                 if not visited[v]:
#                     q.append(e)

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global cnt
    cnt += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)

dfs(1)
# 시작 정점 빼야됨
print(cnt - 1)