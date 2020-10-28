n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

lines = sorted(lines, key=lambda x: x[0])

# LIS
# 각 위치까지의 가장 긴 리스트를 구하기 위한 리스트
result = [[] for _ in range(n)]
for i in range(n):
    if i == 0:
        result[i].append(lines[i][1])
    else:
        # 0 ~ 현재 위치 까지
        for j in range(0, i):
            # 마지막 결과값 < i번째와 연결된 줄
            if result[j][-1] < lines[i][1]:
                if len(result[i]) - 1 < len(result[j]):
                    result[i] = result[j] + [lines[i][1]]
        if not result[i]:
            result[i].append(lines[i][1])
m = 0
for i in range(n):
    m = max(m, len(result[i]))
print(n - m)
