n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

lines = sorted(lines, key=lambda x: x[0])

# LIS
result = [[] for _ in range(n)]
for i in range(n):
    if i == 0:
        result[i].append(lines[i][1])
    else:
        for j in range(0, i):
            if result[j][-1] < lines[i][1]:
                if len(result[i]) - 1 < len(result[j]):
                    result[i] = result[j] + [lines[i][1]]
        if not result[i]:
            result[i].append(lines[i][1])
m = 0
for i in range(n):
    m = max(m, len(result[i]))
print(n - m)
