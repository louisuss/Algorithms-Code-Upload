# 1
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접행렬 초기화
    graph = [[False]*(n+1) for _ in range(n+1)]
    # 작년 순위 정보
    rank_lst = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            # i <- j, 차수 += 1
            graph[rank_lst[i]][rank_lst[j]] = True
            indegree[rank_lst[j]] += 1

    # 올해 변경된 순위 정보
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())

        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 시작
    result = []
    q = deque()

    # 진입 차수가 0인 노드 큐 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상정렬 결과가 오직 1개인지 여부
    cycle = False  # 사이클 존재 여부

    # 정확히 노드개수만큼 반복
    for i in range(n):
        # 큐가 비어 있으면 사이클 발생
        if len(q) == 0:
            cycle = True
            break
        # 가능한 정렬 결과가 여러개
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 1 빼기
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새로 진입차수가 0이되는 노드 큐 삽입
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
