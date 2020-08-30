import sys
# 창구수
num = int(input())
# 고객수
cnt = int(input())
# 고객(도착시간, 소요 시간)
customers = [list(map(int, input().split())) for _ in range(cnt)]


def solution(num, customers):
    customers.reverse()
    wating_time = 0
    available_seat = num
    end_time = []

    while customers:
        # 자리있는 경우
        if available_seat:
            start, end = customers.pop()
            end_time.append(start+end)
            available_seat -= 1
        # 자리없는 경우
        else:
            start, end = customers.pop()
            min_end_time = min(end_time)
            if start < min_end_time:
                wating_time += min_end_time-start
                end_time[end_time.index(min_end_time)] = min_end_time + end
            else:
                end_time[end_time.index(min_end_time)] = start + end                
    return wating_time

print(solution(num, customers))
