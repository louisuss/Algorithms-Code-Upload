# n = sec 추가되는 초
def solution(t, n):
    time_type, time = t.split()
    hour, min, sec = map(int, time.split(':'))

    def add_time(time_type, hour, min, sec, n):
        if time_type == 'PM':
            hour += 12
        added_sec = sec + n

        if added_sec >= 60:
            added_sec %= 60
            min += 1
            if min >= 60:
                min %= 60
                hour += 1
                if hour == 24:
                    hour = 0

        hour = change(hour)
        min = change(min)
        sec = change(added_sec)
        return ':'.join([hour, min, sec])
    
    def change(t):
        if t < 10:
            t = '0'+str(t)
        else:
            t = str(t)
        return t
    return add_time(time_type, hour, min, sec, n)

a = input()
n = int(input())
print(solution(a, n))