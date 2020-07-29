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
        if not msg[idx:idx+length] in dic:
            output.append(dic[msg[idx:idx+length-1]])
            lastIdx += 1
            dic[msg[idx:idx+length]] = lastIdx
            idx += length - 1
            length = 0
        else:
            if idx+length-1 == len(msg):
                output.append(dic[msg[idx:idx+length-1]])
                break

    return output
