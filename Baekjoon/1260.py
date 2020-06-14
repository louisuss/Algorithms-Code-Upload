# BFS / DFS
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]
print(adj)
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

# N, M, V = map(int, input().split())
# graph = dict()
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a] = b
#
# def bfs(graph, start_node):
#     visited = []
#     need_visit = []
#
#     need_visit.append(start_node)
#
#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#     return visited
#
# def dfs(graph, start_node):
#     visited = []
#     need_visit = []
#
#     need_visit.append(start_node)
#
#     while need_visit:
#         node = need_visit.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#     return visited
#
# print(dfs(graph, V))
# print(bfs(graph, V))
