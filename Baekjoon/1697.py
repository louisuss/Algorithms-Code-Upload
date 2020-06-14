# BFS
from collections import deque

MAX = 100001
N, K = map(int, input().split())
arr = [0] * MAX

def bfs():
    q = deque([N])
    while q:
        now_pos = q.popleft()
        if now_pos == K:
            return arr[now_pos]
        # 범위안에 포함 되있고 방문하지 않았다면
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < MAX and not arr[next_pos]:
                arr[next_pos] = arr[now_pos] + 1
                q.append(next_pos)
print(bfs())


