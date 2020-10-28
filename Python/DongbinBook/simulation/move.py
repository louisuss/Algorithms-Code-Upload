dirs = {
    'L': (0,-1),
    'R': (0,1),
    'U': (-1,0),
    'D': (1,0)
}
n = int(input())
dir_arr = list(input().split())
now = [0,0]
area = [[0]*n for _ in range(n)]

for dir in dir_arr:
    dy, dx = dirs[dir]
    ny, nx = dy + now[0], dx + now[1]

    if 0 <= ny < n and 0 <= nx < n:
        now = [ny, nx]

print(now[0]+1, now[1]+1)

