n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

# min
start = arr[1] - arr[0]
# max
end = arr[-1] - arr[0]

while (start <= end):
    # 중간 값
    mid = (start+end) // 2
    # 시작 점
    value = arr[0]
    count = 1
    # 설치 가능 공유기
    for i in range(1, len(arr)):
        # 이전 집에서 해당 거리보다 멀리떨어진 집
        if arr[i] >= value + mid:
            # 공유기 설치된 집
            value = arr[i]
            count += 1
    # 설치 된 집이 더 많은 경우 거리 늘려줌
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
