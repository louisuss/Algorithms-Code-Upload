n, c = map(int, input().split())
home_list = [int(input()) for _ in range(n)]

home_list.sort()

start = home_list[1]-home_list[0] # 시작점에서 최단 거리
end = home_list[-1] - home_list[0] # 시작점에서 최대 거리
len_home = len(home_list) # 집 수
result = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이 거리라 가정
    value = home_list[0] # 시작점 기준
    cnt = 1

    # 현재 공유기 사이 거리(mid)를 기준으로 설치하기
    for i in range(1, len_home):
        if home_list[i] >= value + mid: # 집 위치 >= 기준 집 위치 + 거리 -> 설치 가능
            value = home_list[i] # 기준 위치 이동
            cnt += 1 # 설치한 집 개수 증가 
    # 사용한 공유기가 기준 공유기 보다 크거나 같은 경우
    if cnt >= c:
        # 기준 거리 늘리기
        start = mid + 1
        # 이전 결과 저장 
        result = mid
    # 공유기가 모자른 경우 기준 거리 줄여야함
    else:
        end = mid-1
print(result)
