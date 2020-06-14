n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

# min
start = arr[1] - arr[0]
#max
end = arr[-1] - arr[0]

while (start <= end):
    mid = (start+end) // 2
    value = arr[0]
    count = 1
    # 설치 가능 공유기
    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)