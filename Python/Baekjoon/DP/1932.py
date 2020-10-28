n = int(input())
t = []

for i in range(n):
    t.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        # 맨 왼쪽
        if j == 0:
            t[i][j] = t[i][j] + t[i-1][j]
        # 맨 오른쪽
        elif i == j:
            t[i][j] = t[i][j] + t[i-1][j-1]
        # 중간
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j])+t[i][j]
    k += 1

print(max(t[n-1]))
