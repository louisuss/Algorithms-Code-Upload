R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
result = 0

def bfs(x, y):
    global result
    # 동일한 경우는 한 번만 계산하기 위해 set 사용
    q = set()
    q.add((x, y, A[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0 <= nx < R and 0 <= ny < C and A[nx][ny] not in step:
                # (0,1,"CA"), (1,0,"CA")
                q.add((nx, ny, step + A[nx][ny]))

bfs(0,0)
print(result)
                

