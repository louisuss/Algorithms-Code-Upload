import sys

# 문제 이해에서 어려움

# 수신 가능 영역을 조절
# 집중국의 수신 가능영역의 최솟값
n = int(input())
k = int(input())
positions = list(map(int, input().split()))
positions.sort()

# 정렬된 센서들을 최대 k개의 영역으로 나누는 것
# 각 센서 사이 거리 계산
# 1 3 6 6 7 9
#  2|3|0 1 2
# 가장 긴거리 선택해서 k-1개의 연결고리 제거

if k >= n:
    print(0)
    sys.exit()

distances = []
for i in range(1, n):
    distances.append(positions[i] - positions[i-1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k-1):
    distances[i] = 0
print(sum(distances))
