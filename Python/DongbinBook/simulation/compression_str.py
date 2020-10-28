
s = input()


def solution(s):
    answer = len(s)
    # 1~길이 절반까지 압축 단위를 늘려감
    for step in range(1, len(s)//2+1):
        compressed = ""
        # 기준점. 앞에서부터 step 만큼의 문자열 추출
        prev = s[0:step]
        # 중복 글자수
        cnt = 1

        for j in range(step, len(s), step):
            # 이전 상태와 동일하면 압축 횟수 증가
            if prev == s[j:j+step]:
                cnt += 1
            # 다른 문자열인 경우
            else:
                # 압축 문자열에 추가
                compressed += str(cnt) + prev if cnt >= 2 else prev
                # 기준점 변경
                prev = s[j:j+step]
                # 압축 횟수 초기화
                cnt = 1
        # 남은 문자열에 대해 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

result = len(s)
# 자르는 단위
for i in range(1, len(s)//2+1):
    lst = []
    for j in range(0, len(s), i):
        lst.append(s[j:j+i])

    cnt = 1
    temp = ""
    for j in range(len(lst)-1):
        # 같은 경우 숫자 추가
        if lst[j] == lst[j+1]:
            cnt += 1
        # 다른 경우 숫자가 추가되어있으면 현재 문자열+숫자
        else:
            if cnt >= 2:
                temp += (str(cnt) + lst[j])
                cnt = 1
            else:
                temp += lst[j]
    if cnt >= 2:
        temp += str(cnt) + lst[-1]
    else:
        temp += lst[-1]
    result = min(result, len(temp))
print(result)