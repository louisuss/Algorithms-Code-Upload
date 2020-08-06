def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[0] = 1

    while sum(visited) != n:
        for cost in costs:
            i1, i2, c = cost
            if visited[i1] or visited[i2]:
                if visited[i1] and visited[i2]:
                    continue
                else:
                    visited[i1] = 1
                    visited[i2] = 1
                    answer += c
                    break
    return answer

# def solution(n, costs):
#     answer = 0

#     V = set()
#     for v1, v2, cost in costs:
#         V.add(v1)
#         V.add(v2)
#     sortedCosts = sorted(costs, key=lambda x: x[2])

#     visited = set()

#     visited.add(V.pop())
#     while V:
#         for i in range(len(sortedCosts)):
#             v1, v2, cost = sortedCosts[i]
#             if v1 in visited and v2 in visited:
#                 sortedCosts.pop(i)
#                 break
#             elif v1 in visited or v2 in visited:
#                 if v1 in V:
#                     V.remove(v1)
#                 if v2 in V:
#                     V.remove(v2)
#                 visited.add(v1)
#                 visited.add(v2)
#                 answer += cost
#                 sortedCosts.pop(i)
#                 break

#     return answer

# import heapq as hq
# n = 4
# costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

# def solution(n, costs):
#     answer = 0
#     from_to = [[] for _ in range(n)]
#     visited = [False] * n
#     priority = []

#     for a, b, c in costs:
#         from_to[a].append((b, c))
#         from_to[b].append((a, c))

#     hq.heappush(priority, (0, 0))

#     while False in visited:
#         cost, start = hq.heappop(priority)
#         if visited[start]: continue

#         visited[start] = True
#         answer += cost

#         for end, cost in from_to[start]:
#             if visited[end]: continue
#             else:
#                 hq.heappush(priority, (cost, end))
# =    return answer

# solution(n, costs)
# def solution(n, costs):
#     costs.sort()
#     connect = [costs[0][0]]
#     answer = 0

#     while len(connect) != n:
#         temp =100000000000000000
#         idx = 0
#         # 최소값 찾기
#         for i in range(len(costs)):
#             if costs[i][0] in connect or costs[i][1] in connect:
#                 if costs[i][0] in coonect and costs[i][1] in connect:
#                     continue
#                 if temp > costs[i][2]:
#                     temp = costs[i][2]
#                     idx = i
#         answer += temp
#         connect.append(costs[idx][0])
#         connect.append(costs[idx][1])
#         connect = list(set(connect))
#         consts.pop(idx)
#     return answer
