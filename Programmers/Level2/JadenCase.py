
def solution(s):
    answer = ''
    temp = ''
    for i in s:
        if i == ' ':
            answer += temp.capitalize() + ' '
            temp = ''
            continue
        temp += i
    answer += temp.capitalize()

    return answer
