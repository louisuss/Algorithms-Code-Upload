# 문자열을 리스트로 바꾸기 보다 문자열 자쳬로 슬라이싱 처리하는 것이 더 편한 경우임

def solution(msg):
    # 출력
    output = []

    # 사전
    dic = {chr(v): i for i, v in enumerate(range(ord('A'), ord('Z')+1), 1)}

    idx = 0
    lastIdx = 26
    length = 0
    while True:
        length += 1
        # dic에 해당 문자열이 포함안되어 있는 경우
        if not msg[idx:idx+length] in dic:
            # 이전 값 추가
            output.append(dic[msg[idx:idx+length-1]])
            lastIdx += 1
            # 사전 추가
            dic[msg[idx:idx+length]] = lastIdx
            # 글자 시작 위치
            idx += length - 1
            # 글자 길이 초기화
            length = 0
        else:
            # 마지막 부분 값 추가
            if idx+length-1 == len(msg):
                output.append(dic[msg[idx:idx+length-1]])
                break

    return output
