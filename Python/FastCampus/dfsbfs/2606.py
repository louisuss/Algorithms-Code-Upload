from collections import defaultdict, deque

computer = int(input())
connetion = int(input())
network = defaultdict(list)

for _ in range(connetion):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)


def bfs(start):
    visited = [False] * (computer+1)
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()

        for next in network[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    return visited.count(True)-1  # 시작하는 컴퓨터 빼기


print(bfs(1))
