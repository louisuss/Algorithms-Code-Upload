# LIS

# 무게(너비) 기준 정렬
# dp[i] = 인덱스가 i인 벽돌을 가장 아래에 두었을 때의 최대 높이
# 각 벽돌에 대해 확인하며 dp[i] 갱신
# 0 <= j < i 대해, dp[i] = max(dp[i], dp[j]+height[i]) if width[i] > width[j]
n = int(input()) # 벽돌수

arr = [(0, 0, 0, 0)] # 1부터 시작하기 위해 0 추가
for i in range(1, n+1):
    width, height, weight = map(int, input().split())
    arr.append((i, width, height, weight)) # 번호 추가 

# 무게 정렬
arr.sort(key=lambda x: x[3])

# 인덱스가 i인 벽돌을 가장 아래에 두었을 때의 최대 높이
dp = [0] * (n+1)
for i in range(1, n+1):
    # j 는 i 보다 가벼운 벽돌
    for j in range(i):
        # width 비교
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+arr[i][2])

# 최대 높이
max_value = max(dp)
idx = n
result = []
# dp, arr 인덱스 번호 값 같음
while idx != 0:
    if max_value == dp[idx]:
        result.append(arr[idx][0])  # 번호 추가
        max_value -= arr[idx][2]  # 최대값에 추가한 번호 높이 빼기
    idx -= 1
result.reverse()
print(len(result))
[print(i) for i in result]
