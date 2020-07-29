# 이름이 바뀌면 이전 데이터도 바뀌어야됨
# 최종 이름이 중요
# 1. 데이터 저장
# 2. 변경
# Enter uid1234 Muzi -> 이름 변경될수 있음
# Leave uid1234
# Change uid1234 Muzi


def enterMsg(name):
    return name + "님이 들어왔습니다."


def outMsg(name):
    return name + "님이 나갔습니다."


def changedNickname(record):
    r = {}

    for rec in record:
        rec = list(rec.split(' '))

        if rec[0] == "Enter" or rec[0] == "Change":
            r[rec[1]] = rec[2]

    return r


def solution(record):
    answer = []
    cn = changedNickname(record)

    for rec in record:
        rec = list(rec.split(' '))

        if rec[0] == "Enter":
            answer.append(enterMsg(cn[rec[1]]))
        elif rec[0] == "Leave":
            answer.append(outMsg(cn[rec[1]]))

    return answer
