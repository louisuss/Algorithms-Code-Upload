from collections import defaultdict

# 4
# muc lhr
# jfk muc
# sfo sjc
# lhr sfo
n = int(input())
tickets = [list(input().split()) for _ in range(n)]


def findItinerary(tickets):
    graph = defaultdict(list)
    for f, t in sorted(tickets):
        graph[f].append(t)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('jfk')
    # 맨마지막부터 추가되므로
    return route[::-1]


def findItinerary_upgrade(tickets):
    graph = defaultdict(list)
    for f, t in sorted(tickets, reverse=True):
        graph[f].append(t)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('jfk')
    # 맨마지막부터 추가되므로
    return route[::-1]


def findItinerary_stk(tickets):
    graph = defaultdict(list)
    for f, t in sorted(tickets):
        graph[f].append(t)

    route, stack = [], ['jfk']

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    # 맨마지막부터 추가되므로
    return route[::-1]


print(findItinerary(tickets))
print(findItinerary_upgrade(tickets))
print(findItinerary_stk(tickets))
