# n = kiosk 개수 / customers = [날짜(4-1) - 2월=28일, 시간(01:24:23), 소요시간(1~59분)]
# 고객 키오스크 배치
# 빈 키오스크 - 업무 완료 후 현재 시간까지 운영안된 시간 크고 번호 낮은 곳부터 매칭
# 꽉찬 경우 - 가장 먼저 종료될 키오스크와 매칭, 종료 시간이 같은 경우 번호 낮은 곳과 매칭

def find_empty_kiosk(kiosk, current_time):
    result = []
    for i in range(len(kiosk)):
        month, day, hour, minutes, sec = current_time
        k_month, k_day, k_hour, k_minutes, k_sec = kiosk[i][0]


def find_finish_soon(kiosk, current_time):
    pass


def add_time(current_time, using_time):
    month, day, hour, minutes, sec = current_time
    minutes += using_time

    if minutes > 60:
        minutes %= 60
        hour += 1
        if hour == 24:
            hour = 0
            day += 1
            if month == 2 and day == 29:
                month += 1
                day = 1
            if month in [1, 3, 5, 7, 8, 10, 12]:
                month += 1
                if month == 13:
                    month = 1
                day = 1
            if month in [4, 6, 9, 11]:
                month += 1
                day = 1

    return [month, day, hour, minutes, sec]

# t1 - t2


def minus_time(t1, t2):
    month, day, hour, minutes, sec = t1
    n_month, n_day, n_hour, n_minutes, n_sec = t2

    if sec >= n_sec:
        gap_sec = sec - n_sec
    else:
        minutes -= 1
        gap_sec = (60+sec) - n_sec

    if minutes >= n_minutes:
        gap_minutes = minutes - n_minutes
    else:
        hour -= 1
        gap_minutes = (60+minutes) - n_minutes

    if hour >= n_hour:
        gap_hour = hour - n_hour
    else:
        day -= 1
        gap_hour = (24+hour) - n_hour

    if day >= n_day:
        gap_day = day - n_day
    else:
        pass


def solutions(n, customers):
    kiosk = []

    for customer in customers:
        date, time, using_time = customer
        month, day = map(int, date.split('-'))
        hour, minutes, sec = map(int, time.split(':'))
        using_time = int(using_time)

        current_time = [month, day, hour, minutes, sec]

        if len(kiosk) != n:
            kiosk.append()
