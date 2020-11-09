from collections import deque

MAX = 100001
n, k = map(int, input().split())
arr = [0]*MAX # 시간 기록

def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return arr[now]
        # 모든 경우의 수로 이동 
        for next in [now-1, now+1, now*2]:
            # 범위 안에 있고 방문하지 않은 경우 - 시간+1 해줘서 방문 확인 가능
            if 0 <= next < MAX and not arr[next]:
                arr[next] = arr[now] + 1 # 시간 증가
                q.append(next)

print(bfs())