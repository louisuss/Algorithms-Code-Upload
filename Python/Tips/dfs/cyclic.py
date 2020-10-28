from collections import defaultdict

num_course = int(input())
prerequisites = []


def can_finish(num_course, prerequisites):
    graph = defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()  # 재방문 방지

    def dfs(i):
        # 순환 구조 False
        if i in traced:
            return False

        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    return True
