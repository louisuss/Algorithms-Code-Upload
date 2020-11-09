# 시간 -> 문자열로 바꿔서 계산하면 편함

n, k = map(int, input().split())


def solution1():
    # def check_n(number):
    #     number = str(number)
    #     len_number = len(number)
    #     if len_number == 1:
    #         if int(number) == k:
    #             return True
    #         else:
    #             return False
    #     else:
    #         num_10 = int(number[0])
    #         num_1 = int(number[1])
    #         if num_10 == k or num_1 == k:
    #             return True
    #         else:
    #             return False
    def check_n(number):
        local_number = str(number)
        # 3 이 아니라 03 으로 처리해야 k = 0일 때도 에러 안뜸
        if len(local_number) == 1:
            local_number = '0' + local_number
        if str(k) in local_number:
            return True
        else:
            return False

    cnt = 0
    for hour in range(n+1):
        for minute in range(60):
            for sec in range(60):
                check_hour = check_n(hour)
                check_minute = check_n(minute)
                check_sec = check_n(sec)
                if check_hour or check_minute or check_sec:
                    cnt += 1
    print(cnt)


solution1()


def solution2():
    cnt = 0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                hour = str(h) if h >= 10 else '0' + str(h)
                minute = str(m) if m >= 10 else '0' + str(m)
                sec = str(s) if s >= 10 else '0' + str(s)
                if str(k) in hour + minute + sec:
                    cnt += 1
    print(cnt)


solution2()
