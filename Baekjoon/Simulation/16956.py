# S = 양 / W = 늑대 / D = 울타리

R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ck = False

for i in range(R):
    for j in range(C):
        if A[i][j] == 'W':
            for x, y in zip(dx, dy):
                nx = i+x
                ny = j+y
                if 0 <= nx < R and 0 <= ny < C:
                    if A[nx][ny] == 'S':
                        ck = True
if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if A[i][j] not in 'SW':
                A[i][j] = 'D'

for i in A:
    print(''.join(i))
