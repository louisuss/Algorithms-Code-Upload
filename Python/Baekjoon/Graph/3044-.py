# 1번시작 2번 끝
# 일방통행
# 1~N 마을
# M 개 일방통행 도로
# return 총 경로수
# 9자리 넘으면 뒤의 9자리만 출력
# 무한대 inf - 어떻게 가능??

# 시간 초과...

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**3)
# n = 노드 개수
# m = 간선 개수
n, m = map(int, input().split())
case = 0
roads = defaultdict(list)
inf_ck = False


# A->B
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)


def dfs(n):
    global case
    global inf_ck
    # 키가 n 인 값
    for v in roads[n]:
        if v == 2:
            case += 1
        else:
            # k = 값 -> 키에도 존재하면 일방통행이 아님 - 무한루프가능
            if n in roads[v]:
                inf_ck = True
                return
            dfs(v)


def bfs(n):
    global case
    global inf_ck
    q = deque([n])
    while q:
        temp = roads[q.popleft()]
        for v in temp:
            if v == 2:
                case += 1
            else:
                if n in roads[v]:
                    inf_ck = True
                    return
                if v not in q:
                    q.append(v)


bfs(1)

if inf_ck:
    print("inf")
else:
    if len(str(case)) > 9:
        print(int(str(case)[len(str(case))-9:]))
    else:
        print(case)
