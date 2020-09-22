n, c = map(int, input().split())
location = []
for _ in range(n):
    location.append(int(input()))

location.sort()

# gap 최소값
start = location[1]-location[0]
# gap 최대값
end = location[-1] - location[0]
result = 0

while (start <= end):
    # gap의 중간 값
    mid = (start + end) // 2
    value = location[0]
    cnt = 1

    # mid 값을 이용해 공유기 설치
    for i in range(1, n):
        # 현재위치+gap이 다음집보다 작은 경우. 새로 설치해야함
        if location[i] >= value + mid:
            # 현재위치 갱신
            value = location[i]
            cnt += 1
    # 설치한 공유기가 사용가능 공유기 보다 크거나 같은 경우
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
