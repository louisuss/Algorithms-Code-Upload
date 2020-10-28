N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1, 0], [0, 0, 1, 0, -1]

ans = 10000


def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000
        for w in range(5):
            nx, ny = x+dx[w], y+dy[w]
            flow.append((nx, ny))
            ret += A[nx][ny]
    if len(set(flow)) != 15:
        return 10000
    else:
        return ret


for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            ans = min(ans, ck([i, j, k]))

print(ans)
