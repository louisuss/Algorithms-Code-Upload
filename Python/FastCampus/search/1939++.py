n, m = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(m)]
result = [[0]*(n+1) for _ in range(n+1)]
factory = list(map(int,input().split()))

for info in infos:
    a, b, c = info
    if result[a][b] < c:
        result[a][b] = c
    if result[b][a] < c:
        result[b][a] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            result[a][b] = max(result[a][b], min(result[a][k],result[k][b]))

print(result[factory[0]][factory[1]])

