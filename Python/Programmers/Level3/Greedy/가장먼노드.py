from collections import defaultdict, deque


def bfs(graph, start, distances):
    q = deque([start])
    visited = set([start])

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1


def solution(n, edge):
    # 그래프 만들기
    graph = defaultdict(list)

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    # bfs 탐색 (최단 거리를 구해야 하므로.)
    distances = [0]*(n+1)
    bfs(graph, 1, distances)

    return distances.count(max(distances))

# def solution(n, edge):
#     graph = [[] for _ in range(n+1)]
#     distances = [0] * n
#     visited = [False] * n
#     queue = [0]
#     visited[0] = True

#     for a, b in edge:
#         graph[a-1].append(b-1)
#         graph[b-1].append(a-1)

#     while queue:
#         q = queue.pop(0)

#         for v in graph[q]:
#             if not visited[v]:
#                 visited[v] = True
#                 queue.append(v)
#                 distances[v] = distances[q] + 1

#     distances.sort(reverse=True)
#     return distances.count(distances[0])


print([0]*3)
# from collections import deque


# def bfs(v, visited, adj):
#     # 1과의 거리
#     cnt = 0
#     q = deque([[v, cnt]])

#     while q:
#         v, cnt = q.popleft()
#         # 방문하지 않은 경우
#         if visited[v] == -1:
#             visited[v] = cnt
#             cnt += 1
#             for e in adj[v]:
#                 q.append([e, cnt])


# def solution(n, edge):
#     answer = 0
#     visited = [-1] * (n+1)
#     adj = [[] for _ in range(n+1)]

#     for e in edge:
#         x, y = e[0], e[1]
#         adj[x].append(y)
#         adj[y].append(x)

#     bfs(1, visited, adj)
#     for v in visited:
#         if v == max(visited):
#             answer += 1
#     return answer
