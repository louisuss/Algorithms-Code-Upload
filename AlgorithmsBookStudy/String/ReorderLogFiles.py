# 1. 로그 가장 앞부분은 식별자
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 옴 -> 문자로그 + 숫자로그
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 함 -> 문자 정렬 (식별자 이외 부분 기준 정렬, 식별자 기준 정렬)
# 4. 숫자 로그는 입력 순서대로 한다. -> 정렬 필요 없음

def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        # log.split() -> ['dig1', '8', '1', '5', '1']
        # 주어지는 logs 리스트의 1번 인덱스가 문자거나 숫자임
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 정렬 기준 설정: x.split()[1:] -> 식별자 뒤의 나오는 문자 기준, x.split()[0] -> 식별자 기준
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))
